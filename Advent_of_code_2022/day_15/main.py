import os
import re
import itertools as it

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def part_1(sensor_data):
    y_line = 2000000
    impossible_locations = set()
    beacons = set()
    for sensor in sensor_data:
        sensor_x, sensor_y = sensor[:2]
        beacon_x, beacon_y = sensor[2:]
        beacons.add((beacon_x, beacon_y))
        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        distance_to_y = abs(sensor_y - y_line)
        if distance_to_y <= distance:
            impossible_range = list(it.zip_longest(range(
                sensor_x - distance + distance_to_y, sensor_x + distance - distance_to_y+1),[y_line], fillvalue=y_line))
            impossible_locations.update(impossible_range)

    return len(impossible_locations-beacons)


def calcualte_distance(sensor, point):
    sensor_x, sensor_y, _ = sensor
    point_x, point_y = point
    return abs(sensor_x - point_x) + abs(sensor_y - point_y)


def part_2(sensor_data):
    sensors = []
    for sensor in sensor_data:
        sensor_x, sensor_y = sensor[:2]
        becon_x, becon_y = sensor[2:]
        sensor_distance = abs(sensor_x - becon_x) + abs(sensor_y - becon_y)
        sensors.append((sensor_x, sensor_y, sensor_distance))

    
    intersections = set()


    # Find all points where the border around each sensor intersects with the border around all other sensors
    for i in range(len(sensors)):
        x_1, y_1, d_1 = sensors[i]
        for j in range(i+1,len(sensors)):
            # Using the equation for a line y - y_1 = a(x - x_1). Here a is always 1 or -1
            # And generating all lines that can possible have an intersection with each other
            # Then calculates where they intersect and checks if their intersection is in range of both sensors
            x_2, y_2, d_2 = sensors[j]
            x_1_right = x_1 + d_1
            x_1_left = x_1 - d_1
            x_2_right = x_2 + d_2
            x_2_left = x_2 - d_2

            x_intersections = \
                [
                    (x_1_right + y_1 + x_2_left - y_2)/2,
                    (x_1_right + y_1 + x_2_right - y_2)/2,
                    (x_1_left + y_1 + x_2_left - y_2)/2,
                    (x_1_left + y_1 + x_2_right - y_2)/2,
                    (x_1_right + y_1 - x_2_left + y_2)/2,
                    (x_1_right + y_1 - x_2_right + y_2)/2,
                    (x_1_left + y_1 - x_2_left + y_2)/2,
                    (x_1_left + y_1 - x_2_right + y_2)/2,
                ]
            y_intersections = \
                [
                    -x_intersections[0] + y_1 + x_1_right,
                    -x_intersections[1] + y_1 + x_1_right,
                    -x_intersections[2] + y_1 + x_1_left,
                    -x_intersections[3] + y_1 + x_1_left,
                    x_intersections[4] + y_1 - x_1_right,
                    x_intersections[5] + y_1 - x_1_right,
                    x_intersections[6] + y_1 - x_1_left,
                    x_intersections[7] + y_1 - x_1_left,

                ]
                
            for x, y in zip(x_intersections, y_intersections):
                if calcualte_distance(sensors[i], (x, y)) <= d_1 and calcualte_distance(sensors[j], (x, y)) <= d_2:
                    intersections.add((int(x), int(y)))
            

    # Check all the intersections to see if there is a point around it which is out of range from all sensors

    for intersection in intersections:
        x, y = intersection
        for point in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            for sensor in sensors:
                sensor_x, sensor_y, sensor_distance = sensor
                if calcualte_distance(sensor, point) <= sensor_distance:
                    break
            else:
                if (0 <= point[0] <= 4000000) and (0 <= point[1] <= 4000000):
                    return point



if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().splitlines()
        data = [[int(i) for i in re.findall(r"(-?\d+)", line)] for line in data]
    print("Part 1:", part_1(data))
    beacon_position = part_2(data)
    print("Part 2:", beacon_position[0]*4000000 + beacon_position[1])

