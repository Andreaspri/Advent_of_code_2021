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
            traveler = Traveler([random.choice(cave) for i in range(self.minutes_to_live)])
            traveler.genome.insert(0, self.start)
            self.travelers.append(traveler)

    def make_new_generation(self):
        self.generation += 1
        new_travelers = []
        self.travelers.sort(key=lambda x: x.score, reverse=True)
        cave = list(self.cave.keys())
        cave.remove("AA")
        parents = self.travelers[:len(self.travelers)//5]
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
            minutes_left = self.minutes_to_live
            pressure = 0
            active_pressure_gauges = []
            activated = {}
            old_position = traveler.genome[0]
            for position in traveler.genome[1:]:
                if position not in activated and position != old_position:
                        minutes_used = self.cave[old_position]["tunnels"][position]+1
                        if minutes_left < minutes_used:
                            pressure += sum(active_pressure_gauges)*minutes_left
                            break
                        pressure += sum(active_pressure_gauges)*minutes_used
                        active_pressure_gauges.append(self.cave[position]["flow_rate"])
                        activated[position] = True
                        old_position = position
                        minutes_left -= minutes_used


                if minutes_left <= 0:
                    break

        traveler.score = pressure
        if pressure > self.best_traveler_score:
            self.best_traveler_score = pressure
            self.best_traveler = traveler



class Traveler:
    def __init__(self, genome, mutation_rate=0.3):
        self.genome = genome
        self.score = 0
        self.opened_valves = []
        self.mutation_rate = mutation_rate

    def crossover(self, traveler1):
        genome = [self.genome[0]]
        for i in range(1, len(traveler1.genome)):
            if random.random() < 0.5:
                genome.append(traveler1.genome[i])
            else:
                genome.append(self.genome[i])
        return Traveler(genome)

    def mutate(self, cave: list):
        for i in range(1, len(self.genome)):
            if random.random() <= self.mutation_rate:
                self.genome[i] = random.choice(cave)


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


def part_1(valves, generations=1000, minutes_to_live=30, cave=None):
    if not cave:
        cave = Cave('AA', valves, minutes_to_live)
        cave.make_start_generation()
    for i in range(generations):
        cave.score_travelers()
        cave.make_new_generation()
        if i % 1000 == 0:
            if cave.best_traveler:
                print(f'Generation: {cave.generation}, Best score: {cave.best_traveler_score}')
    print(cave.best_traveler_score)
    return cave



if __name__ == '__main__':
    pool = multiprocessing.Pool()
    with open('data.txt') as f:
        data = f.read().splitlines()
    
    all_valves = parse_data(data)
    
    print("Part 1:", part_1(all_valves, generations=100000, minutes_to_live=30).best_traveler_score)
