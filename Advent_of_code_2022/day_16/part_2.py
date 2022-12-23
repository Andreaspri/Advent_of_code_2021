import os
import re
import multiprocessing
import random
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Cave:
    def __init__(self, start, cave: dict, minutes_to_live, num_travelers=100):
        self.start = start
        self.cave = cave
        self.travelers = []
        self.generation = 0
        self.best_traveler = None
        self.best_traveler_score = 0
        self.minutes_to_live = minutes_to_live
        self.num_travelers = num_travelers



    def make_start_generation(self):
        cave = list(self.cave.keys())
        cave.remove("AA")
        for i in range(self.num_travelers):
            # Random chice from the cave with np
            genome_1 = [random.choice(cave) for i in range(min(self.minutes_to_live//2, len(cave)))]
            genome_2 = [random.choice(cave) for i in range(min(self.minutes_to_live//2, len(cave)))]
            traveler = Traveler(genome_1, genome_2)
            traveler.genome_1.insert(0, self.start)
            traveler.genome_2.insert(0, self.start)
            self.travelers.append(traveler)

    def make_new_generation(self):
        self.generation += 1
        new_travelers = []
        self.travelers.sort(key=lambda x: x.score, reverse=True)
        cave = list(self.cave.keys())
        cave.remove("AA")
        # Only keep the best 10% of the travelers
        # This narrows down to a more specific path
        # This works with my approach of starting many processes
        parents = self.travelers[:len(self.travelers)//10]
        new_travelers.extend(parents)
        while len(new_travelers) < self.num_travelers:
            traveler1 = random.choice(parents)
            traveler2 = random.choice(parents)
            new_traveler1 = traveler1.crossover(traveler2)
            new_traveler2 = traveler2.crossover(traveler1)
            new_traveler1.mutate(cave)
            new_traveler2.mutate(cave)
            new_travelers.extend([new_traveler1, new_traveler2])
        self.travelers = new_travelers
        


    def score_travelers(self):
        for traveler in self.travelers:
            pressure = 0
            active_pressure_gauges = []
            activated = {}
            genome_1 = traveler.genome_1
            genome_2 = traveler.genome_2
            order = []

            minutes_used = 0
            old_position = genome_1[0]
            for i in range(len(genome_1)):
                if old_position == genome_1[i]:
                    continue
                minutes_used += self.cave[old_position]["tunnels"][genome_1[i]]+1
                order.append((genome_1[i], minutes_used))
                old_position = genome_1[i]
            
            minutes_used = 0
            old_position = genome_2[0]
            for i in range(len(genome_2)):
                if old_position == genome_2[i]:
                    continue
                minutes_used += self.cave[old_position]["tunnels"][genome_2[i]]+1
                order.append((genome_2[i], minutes_used))
                old_position = genome_2[i]

            order.sort(key=lambda x: x[1])

            old_time = 0
            for valve, time in order:
                if valve in activated:
                    continue
                if time > self.minutes_to_live:
                    rest = self.minutes_to_live - old_time
                    pressure += sum(active_pressure_gauges)*rest
                    break
                diff = time-old_time
                if diff == 0:
                    active_pressure_gauges.append(self.cave[valve]["flow_rate"])
                    activated[valve] = True
                    continue
                    
                pressure += sum(active_pressure_gauges)*diff
                active_pressure_gauges.append(self.cave[valve]["flow_rate"])
                activated[valve] = True
                old_time = time
            
            traveler.score = pressure
            if pressure > self.best_traveler_score:
                self.best_traveler_score = pressure
                self.best_traveler = traveler







class Traveler:
    def __init__(self, genome_1, genome_2, mutation_rate=0.3):
        self.genome_1 = genome_1
        self.genome_2 = genome_2
        self.score = 0
        self.opened_valves = []
        self.mutation_rate = mutation_rate

    def crossover(self, traveler1):
        genome_1 = [self.genome_1[0]]
        genome_2 = [self.genome_2[0]]
        for i in range(1, len(traveler1.genome_1)):
            if random.random() < 0.5:
                genome_1.append(traveler1.genome_1[i])
                genome_2.append(traveler1.genome_2[i])
            else:
                genome_1.append(self.genome_1[i])
                genome_2.append(self.genome_2[i])


        return Traveler(genome_1, genome_2)


    def mutate(self, cave: list):
        for i in range(1, len(self.genome_1)):
            if random.random() <= self.mutation_rate:
                self.genome_1[i] = random.choice(cave)
                self.genome_2[i] = random.choice(cave)


def parse_data(data):
    valves = {}
    for line in data:
        result = re.match(r'Valve (\w{2}) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)
        valve, flow_rate, tunnels = result.groups()
        valves[valve] = {'flow_rate': int(flow_rate), 'tunnels': tunnels.split(', ')}

    # Putting in the edges to the graph
    w = [[float("inf") for i in range(len(valves))] for j in range(len(valves))]
    for i, valve1 in enumerate(valves):
        for j, valve2 in enumerate(valves):
            if i == j:
                w[i][j] = 0
            if valve2 in valves[valve1]['tunnels']:
                w[i][j] = 1
    
    # Floyd-Warshall
    for k in range(len(valves)):
        for i in range(len(valves)):
            for j in range(len(valves)):
                w[i][j] = min(w[i][j], w[i][k] + w[k][j])

    # Removing all the valves that are not connected to the start and adding the weights
    for i, valve1 in enumerate(valves):
        for j, valve2 in enumerate(valves):
            if i == j:
                continue
            if valves[valve2]["flow_rate"] > 0:
                try:
                        valves[valve1]["tunnels"].remove(valve2)
                except:
                    pass
                finally:
                    valves[valve1]["tunnels"].append((valve2, w[i][j]))
            else:
                try:
                    valves[valve1]["tunnels"].remove(valve2)
                except:
                    pass

        valves[valve1]["tunnels"] = {valve: value for valve, value in valves[valve1]["tunnels"]}
    
    # Remove all valves with flow rate greater than 0
    return {valve: value for valve, value in valves.items() if value["flow_rate"] > 0 or valve == 'AA'}


def part_2(valves, generations=1000, minutes_to_live=26, cave=None):
    if not cave:
        cave = Cave('AA', valves, minutes_to_live)
        cave.make_start_generation()
    for i in range(generations):
        cave.score_travelers()
        cave.make_new_generation()
        if i % 1000 == 0:
            if cave.best_traveler:
                print(f'Generation: {cave.generation}, Best score: {cave.best_traveler_score}')

    return cave



if __name__ == '__main__':
    pool = multiprocessing.Pool()
    with open('data.txt') as f:
        data = f.read().splitlines()
    
    all_valves = parse_data(data)
    best_score = 0

    result = max(pool.starmap(part_2, [(all_valves, 10000, 26) for i in range(10)]), key=lambda x: x.best_traveler_score)

    print("Part 2:", result.best_traveler_score)
