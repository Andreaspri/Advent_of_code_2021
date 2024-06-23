



def parse_data() -> tuple[dict,list]:
    with open("input.txt", 'r') as f:
        data = f.readlines()
    seeds = [int(i) for i in data[0].split("seeds: ")[1].split(" ")]
    maps = {}

    # Removing seeds
    data.pop(0)

    switch = False
    for i, line in enumerate(data):
        if line == '\n':
            switch = True
            continue
        if switch:
            context = data[i].split(":")[0]
            maps[context] = []
            switch = False
            continue
        
        maps[context].append(tuple(int(i) for i in line.split(" ")))


    return maps, seeds




def get_destination(source: int, targets: list[tuple], reverse=False) -> int:

    for target in targets:
        if reverse:
            src_rng, dest_rng, len_rng = target
        else:
            dest_rng, src_rng, len_rng = target

        # If the diff is 0 or greater and source is less than the source range start + the range lenght it belongs at position dest_rng + diff
        # Else it belongs to destination = source
        diff = source - src_rng
        if diff >= 0 and source < src_rng + len_rng:
            return dest_rng + diff
        
    # No matches maps to same number
    return source



def map_range(s_start: int, s_stop: int, m_start: int, m_stop: int, d_start: int, d_stop: int) -> list[tuple]:

    # Source is forexample the seed start and stop for one range. Middle is where it maps before it get to destination.
    # Destination is the stop where it ends

    # The source lies in the middle of the middle step, case 1
    if m_start <= s_start <= m_stop and m_start <= s_stop <= m_stop:
        return [((s_start-m_start)+d_start, (s_stop-m_start)+d_start)]
    
    # The source is completly over the middle, case 2
    elif s_start <= m_start <= s_stop and s_start <= m_stop <= s_stop:
        base = [(d_start, d_stop)]
        if s_start != m_start:
            base.append((s_start, m_start-1))
        if s_stop != m_stop:
            base.append((m_start+1, s_stop))
        return base
    
    # Case when source is partially overlaping middle on the right side, case 3
    elif m_start <= s_start <= m_stop and s_stop > m_stop:
        return [((s_start-m_start)+d_start, d_stop), (m_stop+1,s_stop)]

    # Case when source is partially overlaping middle on the left side, case 4
    elif s_start < m_start and m_start <= s_stop < m_stop:
        return [(d_start, (s_stop-m_start)+d_start), (s_start, m_start-1)]
    
    # Case when no overlap at all
    elif (s_start < m_start and s_stop < m_start) or (s_start > m_stop and s_stop > m_stop):
        return False
        #return s_start, s_stop
    
    # Case when i fucked up
    else:
        print(f"s_start: {s_start}, s_stop: {s_stop}")
        print(f"m_start: {m_start}, m_stop: {m_stop}")
        print(f"d_start: {d_start}, d_stop: {d_stop}")
        raise "You fucked up"


def part1(maps: dict, seeds: list) -> int:
    
    locations = []

    for seed in seeds:
        curr = seed
        for m_rng in maps.values():
            curr = get_destination(curr, m_rng)
        locations.append(curr)

    return min(locations)



def part2(maps: dict, seeds: list) -> int:

    location_ranges = []

    for i in range(0,len(seeds),2):
        seed_start = seeds[i]
        seed_stop = seeds[i] + seeds[i+1] - 1

        temp_curr_ranges = set()
        temp_curr_ranges.add((seed_start,seed_stop))
         
        for m_rngs in maps.values():
            curr_ranges = temp_curr_ranges
            temp_curr_ranges = set()
            while curr_ranges:
                s_range = curr_ranges.pop()
                miss_c = 0
                curr_start, curr_stop = s_range
                for m_rng in m_rngs:

                    d_start, m_start, lenght = m_rng
                    result = map_range(curr_start, curr_stop, m_start, m_start+lenght-1, d_start, d_start+lenght-1)
                    
                    if result is not False:
                        temp_curr_ranges.add(result[0])
                        if len(result) > 1:
                            curr_ranges.add(result[1])
                            try:
                                curr_ranges.add(result[2])
                            except IndexError:
                                pass
                    else:
                        miss_c += 1
                if miss_c == len(m_rngs):
                    temp_curr_ranges.add(s_range)
    
        location_ranges += [i for i in temp_curr_ranges]

    return location_ranges




if __name__=='__main__':
    maps, seeds = parse_data()

    print("Part 1:", part1(maps, seeds))

    print("Part 2:", min(part2(maps, seeds), key=lambda x: x[1])[0])
