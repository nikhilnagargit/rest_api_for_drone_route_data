from matplotlib import pyplot as plt
import math


def next_cell_selection_from_source_clockwise(source_x, source_y):
    '''Clockwise direction follows'''
    possible_steps, distance_list = [], []
    try:
        coordinates = []
        if (water_matrix[source_x-1][source_y] == 1 or forest_matrix[source_x-1][source_y] == 1 or population_matrix[source_x-1][source_y] <= threshold_population) and building_matrix[source_x-1][source_y] == 0 and traps1[source_x-1][source_y] == 0:
            if 0 <= source_x-1 and 0 <= source_y:
                coordinates.append(source_x-1)
                coordinates.append(source_y)
                if type_of_distance:
                    distance = euclid(source_x-1, source_y, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(source_x-1, source_y, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass

    try:
        coordinates = []
        if (water_matrix[source_x - 1][source_y+1] == 1 or forest_matrix[source_x - 1][source_y+1] == 1 or
                population_matrix[source_x - 1][source_y+1] <= threshold_population) and building_matrix[source_x - 1][source_y+1] == 0 and traps1[source_x - 1][source_y+1] == 0:
            if 0 <= source_x-1 and 0 <= source_y+1:
                coordinates.append(source_x - 1)
                coordinates.append(source_y+1)
                if type_of_distance:
                    distance = euclid(source_x - 1, source_y+1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(
                        source_x - 1, source_y+1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass

    try:
        coordinates = []
        if (water_matrix[source_x][source_y+1] == 1 or forest_matrix[source_x][source_y+1] == 1 or
                population_matrix[source_x][source_y+1] <= threshold_population) and building_matrix[source_x][source_y+1] == 0 and traps1[source_x][source_y+1] == 0:
            if 0 <= source_x and 0 <= source_y+1:
                coordinates.append(source_x)
                coordinates.append(source_y+1)
                if type_of_distance:
                    distance = euclid(source_x, source_y+1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(source_x, source_y+1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass

    try:
        coordinates = []
        if (water_matrix[source_x+1][source_y+1] == 1 or forest_matrix[source_x+1][source_y+1] == 1 or
                population_matrix[source_x+1][source_y+1] <= threshold_population) and building_matrix[source_x+1][source_y+1] == 0 and traps1[source_x+1][source_y+1] == 0:
            if 0 <= source_x+1 and 0 <= source_y+1:
                coordinates.append(source_x+1)
                coordinates.append(source_y+1)
                if type_of_distance:
                    distance = euclid(source_x+1, source_y+1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(source_x+1, source_y+1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass

    try:
        coordinates = []
        if (water_matrix[source_x+1][source_y] == 1 or forest_matrix[source_x+1][source_y] == 1 or
                population_matrix[source_x+1][source_y] <= threshold_population) and building_matrix[source_x+1][source_y] == 0 and traps1[source_x+1][source_y] == 0:
            if 0 <= source_x+1 and 0 <= source_y:
                coordinates.append(source_x+1)
                coordinates.append(source_y)
                if type_of_distance:
                    distance = euclid(source_x+1, source_y, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(source_x+1, source_y, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass

    try:
        coordinates = []
        if (water_matrix[source_x+1][source_y-1] == 1 or forest_matrix[source_x+1][source_y-1] == 1 or
                population_matrix[source_x+1][source_y-1] <= threshold_population) and building_matrix[source_x+1][source_y-1] == 0 and traps1[source_x+1][source_y-1] == 0:
            if 0 <= source_x+1 and 0 <= source_y-1:
                coordinates.append(source_x+1)
                coordinates.append(source_y-1)
                if type_of_distance:
                    distance = euclid(source_x+1, source_y-1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(source_x+1, source_y-1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass

    try:
        coordinates = []
        if (water_matrix[source_x][source_y-1] == 1 or forest_matrix[source_x][source_y-1] == 1 or
                population_matrix[source_x][source_y-1] <= threshold_population) and building_matrix[source_x][source_y-1] == 0 and traps1[source_x][source_y-1] == 0:
            if 0 <= source_x and 0 <= source_y-1:
                coordinates.append(source_x)
                coordinates.append(source_y-1)
                if type_of_distance:
                    distance = euclid(source_x, source_y-1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(source_x, source_y-1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass

    try:
        coordinates = []
        if (water_matrix[source_x-1][source_y-1] == 1 or forest_matrix[source_x-1][source_y-1] == 1 or
                population_matrix[source_x-1][source_y-1] <= threshold_population) and building_matrix[source_x-1][source_y-1] == 0 and traps1[source_x-1][source_y-1] == 0:
            if 0 <= source_x-1 and 0 <= source_y - 1:
                coordinates.append(source_x-1)
                coordinates.append(source_y-1)
                if type_of_distance:
                    distance = euclid(source_x-1, source_y-1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(source_x-1, source_y-1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass
    # print(source_x,source_y)
    return possible_steps, distance_list


def next_cell_selection_from_source_anti_clockwise(source_x, source_y):
    '''Anti-Clockwise direction follows'''
    possible_steps, distance_list = [], []
    try:
        coordinates = []
        if (water_matrix[source_x-1][source_y-1] == 1 or forest_matrix[source_x-1][source_y-1] == 1 or
                population_matrix[source_x-1][source_y-1] <= threshold_population) and building_matrix[source_x-1][source_y-1] == 0 and traps2[source_x-1][source_y-1] == 0:
            if 0 <= source_x-1 and 0 <= source_y - 1:
                coordinates.append(source_x-1)
                coordinates.append(source_y-1)
                if type_of_distance:
                    distance = euclid(source_x-1, source_y-1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(source_x-1, source_y-1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass

    try:
        coordinates = []
        if (water_matrix[source_x][source_y-1] == 1 or forest_matrix[source_x][source_y-1] == 1 or
                population_matrix[source_x][source_y-1] <= threshold_population) and building_matrix[source_x][source_y-1] == 0 and traps2[source_x][source_y-1] == 0:
            if 0 <= source_x and 0 <= source_y-1:
                coordinates.append(source_x)
                coordinates.append(source_y-1)
                if type_of_distance:
                    distance = euclid(source_x, source_y-1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(source_x, source_y-1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass

    try:
        coordinates = []
        if (water_matrix[source_x+1][source_y-1] == 1 or forest_matrix[source_x+1][source_y-1] == 1 or
                population_matrix[source_x+1][source_y-1] <= threshold_population) and building_matrix[source_x+1][source_y-1] == 0 and traps2[source_x+1][source_y-1] == 0:
            if 0 <= source_x+1 and 0 <= source_y-1:
                coordinates.append(source_x+1)
                coordinates.append(source_y-1)
                if type_of_distance:
                    distance = euclid(source_x+1, source_y-1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(source_x+1, source_y-1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass

    try:
        coordinates = []
        if (water_matrix[source_x+1][source_y] == 1 or forest_matrix[source_x+1][source_y] == 1 or
                population_matrix[source_x+1][source_y] <= threshold_population) and building_matrix[source_x+1][source_y] == 0 and traps2[source_x+1][source_y] == 0:
            if 0 <= source_x+1 and 0 <= source_y:
                coordinates.append(source_x+1)
                coordinates.append(source_y)
                if type_of_distance:
                    distance = euclid(source_x+1, source_y, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(source_x+1, source_y, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass

    try:
        coordinates = []
        if (water_matrix[source_x+1][source_y+1] == 1 or forest_matrix[source_x+1][source_y+1] == 1 or
                population_matrix[source_x+1][source_y+1] <= threshold_population) and building_matrix[source_x+1][source_y+1] == 0 and traps2[source_x+1][source_y+1] == 0:
            if 0 <= source_x+1 and 0 <= source_y+1:
                coordinates.append(source_x+1)
                coordinates.append(source_y+1)
                if type_of_distance:
                    distance = euclid(source_x+1, source_y+1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(source_x+1, source_y+1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass

    try:
        coordinates = []
        if (water_matrix[source_x][source_y+1] == 1 or forest_matrix[source_x][source_y+1] == 1 or
                population_matrix[source_x][source_y+1] <= threshold_population) and building_matrix[source_x][source_y+1] == 0 and traps2[source_x][source_y+1] == 0:
            if 0 <= source_x and 0 <= source_y+1:
                coordinates.append(source_x)
                coordinates.append(source_y+1)
                if type_of_distance:
                    distance = euclid(source_x, source_y+1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(source_x, source_y+1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass

    try:
        coordinates = []
        if (water_matrix[source_x - 1][source_y+1] == 1 or forest_matrix[source_x - 1][source_y+1] == 1 or
                population_matrix[source_x - 1][source_y+1] <= threshold_population) and building_matrix[source_x - 1][source_y+1] == 0 and traps2[source_x - 1][source_y+1] == 0:
            if 0 <= source_x-1 and 0 <= source_y+1:
                coordinates.append(source_x - 1)
                coordinates.append(source_y+1)
                if type_of_distance:
                    distance = euclid(source_x - 1, source_y+1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(
                        source_x - 1, source_y+1, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass

    try:
        coordinates = []
        if (water_matrix[source_x-1][source_y] == 1 or forest_matrix[source_x-1][source_y] == 1 or population_matrix[source_x-1][source_y] <= threshold_population) and building_matrix[source_x-1][source_y] == 0 and traps2[source_x-1][source_y] == 0:
            if 0 <= source_x-1 and 0 <= source_y:
                coordinates.append(source_x-1)
                coordinates.append(source_y)
                if type_of_distance:
                    distance = euclid(source_x-1, source_y, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                else:
                    distance = manhattan(source_x-1, source_y, end_x, end_y)
                    distance_list.append(distance)
                    coordinates.append(distance)
                possible_steps.append(coordinates)
    except:
        pass

    #print(source_x, source_y)
    return possible_steps, distance_list


def source_to_destination_clockwise():
    global show, track
    temp_source_x, temp_source_y = start_x, start_y
    temp_destination_x, temp_destination_y = end_x, end_y

    distance = 0  # initial reference
    if type_of_distance:
        distance = euclid(temp_source_x, temp_source_y,
                          temp_destination_x, temp_destination_y)
    else:
        distance = manhattan(temp_source_x, temp_source_y,
                             temp_destination_x, temp_destination_y)
    # print(distance)
    while distance > 0:
        if temp_source_x == temp_destination_x and temp_source_y == temp_destination_y:
            distance = 0
        else:
            possible_steps, possible_distance = next_cell_selection_from_source_clockwise(
                temp_source_x, temp_source_y)
            possible_distance.sort()
            # print(possible_steps)
            if len(possible_steps) == 0:
                print("Not Possible")
                show = False
                break
            for i in possible_steps:
                if possible_distance[0] == i[2]:
                    if [i[0], i[1]] in track:
                        #print("loop",[i[0], i[1]])
                        traps1[i[0]][i[1]] = 1
                        temp_source_x, temp_source_y = start_x, start_y
                        track.clear()
                        track.append([start_x, start_y])
                        break
                    else:
                        track.append([i[0], i[1]])
                        temp_source_x, temp_source_y = i[0], i[1]
                        break
    print("S-D Clockwise")
    print("Distance = ", total_distance(track), "meters")
    print("Matrix Coordinate Path :")
    print(track)


def source_to_destination_anti_clockwise():
    global show
    temp_source_x, temp_source_y = start_x, start_y
    temp_destination_x, temp_destination_y = end_x, end_y

    distance = 0  # initial reference
    if type_of_distance:
        distance = euclid(temp_source_x, temp_source_y,
                          temp_destination_x, temp_destination_y)
    else:
        distance = manhattan(temp_source_x, temp_source_y,
                             temp_destination_x, temp_destination_y)
    # print(distance)
    while distance > 0:
        if temp_source_x == temp_destination_x and temp_source_y == temp_destination_y:
            distance = 0
        else:
            possible_steps, possible_distance = next_cell_selection_from_source_anti_clockwise(
                temp_source_x, temp_source_y)
            possible_distance.sort()
            # print(possible_steps)
            if len(possible_steps) == 0:
                print("Not Possible")
                show = False
                break
            for i in possible_steps:
                if possible_distance[0] == i[2]:
                    if [i[0], i[1]] in track:
                        #print("loop",[i[0], i[1]])
                        traps2[i[0]][i[1]] = 1
                        temp_source_x, temp_source_y = start_x, start_y
                        track.clear()
                        track.append([start_x, start_y])
                        break
                    else:
                        track.append([i[0], i[1]])
                        temp_source_x, temp_source_y = i[0], i[1]
                        break
    print("S-D Anti-Clockwise")
    print("Distance = ", total_distance(track), "meters")
    print("Matrix Coordinate Path :")
    print(track)


def total_distance(path):
    total = 0.0
    for count in range(0, len(path)-1):
        total += euclid(path[count][0], path[count][1],
                        path[count+1][0], path[count+1][1])
    return total*size_of_grid


def euclid(source_x, source_y, destination_x, destination_y):
    x_distance = abs(destination_x - source_x)
    y_distance = abs(destination_y - source_y)
    distance = math.sqrt(x_distance*x_distance + y_distance*y_distance)
    return distance


'''Manhattan distance'''


def manhattan(source_x, source_y, destination_x, destination_y):
    x_distance = abs(destination_x - source_x)
    y_distance = abs(destination_y - source_y)
    distance = x_distance + y_distance
    return distance


###################################################################################################
'''Main Function '''
###################################################################################################


def find_shortest_path(matrix):
    global output, rows, columns, water_matrix, forest_matrix, population_matrix, building_matrix
    global latitude_matrix, longitude_matrix, traps1, traps2, threshold_population, type_of_distance
    global start_x, start_y, end_x, end_y, size_of_grid, show, track
    output = matrix
    ans = {}
    rows, columns = len(output), len(output[0])
    water_matrix = [[0 for i in range(columns)] for j in range(rows)]
    forest_matrix = [[0 for i in range(columns)] for j in range(rows)]
    population_matrix = [[0 for i in range(columns)] for j in range(rows)]
    building_matrix = [[0 for i in range(columns)] for j in range(rows)]
    latitude_matrix = [[0 for i in range(columns)] for j in range(rows)]
    longitude_matrix = [[0 for i in range(columns)] for j in range(rows)]

    threshold_population = 0.5  # Threshold Population density
    type_of_distance = True  # True = Euclidean Distance and False = Manhattan Distance
    start_x, start_y = 0, 0  # source matrix position
    end_x, end_y = len(water_matrix)-1, len(water_matrix[0])-1
    size_of_grid = 11  # size of grid is the dimension of grid by default it is 11m*11m
    for row in range(0, rows):
        for column in range(0, columns):
            water_matrix[row][column] = output[row][column]['w']
            forest_matrix[row][column] = output[row][column]['f']
            if(output[row][column]['s_h'] == 1 or output[row][column]['c'] == 1):
                building_matrix[row][column] = 1
            else:
                building_matrix[row][column] = 0
            population_matrix[row][column] = output[row][column]['p']
            latitude_matrix[row][column] = output[row][column]['lat']
            longitude_matrix[row][column] = output[row][column]['lon']

    traps1 = [[0 for i in range(len(water_matrix[0]))]
              for j in range(len(water_matrix))]  # Trap Matrix
    traps2 = [[0 for i in range(len(water_matrix[0]))]
              for j in range(len(water_matrix))]  # Trap Matrix

    '''Source position restriction check'''
    water_matrix[start_x][start_y] = 1
    forest_matrix[start_x][start_y] = 1
    population_matrix[start_x][start_y] = 0
    building_matrix[start_x][start_y] = 0

    '''Destination position restriction check'''
    water_matrix[end_x][end_y] = 1
    forest_matrix[end_x][end_y] = 1
    population_matrix[end_x][end_y] = 0
    building_matrix[end_x][end_y] = 0

    plt.scatter(start_y, len(water_matrix)-1-start_x, s=100)
    plt.scatter(end_y, len(water_matrix)-1-end_x, s=100)

    show = True
    track = [[start_x, start_y]]
    source_to_destination_clockwise()

    if show:
        x, y = [], []
        for i in track:
            x.append(i[1])
            y.append(len(water_matrix)-1-i[0])
        plt.plot(x, y, label="S-D Clockwise")
    show = True

    lat_long_path = []
    for i in range(0, len(track)):
        lat_long_path.append([latitude_matrix[track[i][0]][track[i][1]],
                              longitude_matrix[track[i][0]][track[i][1]]])
    print("Latitude & Longitude Coordinate Path :")
    print(lat_long_path)
    print("\n")
    ans["clockwise_path"] = lat_long_path.copy()
    lat_long_path.clear()
    track.clear()

    track.append([start_x, start_y])

    source_to_destination_anti_clockwise()
    if show:
        x, y = [], []
        for i in track:
            x.append(i[1])
            y.append(len(water_matrix)-1-i[0])
        plt.plot(x, y, label="S-D Anti-Clockwise")

    show = True
    lat_long_path = []
    for i in range(0, len(track)):
        lat_long_path.append([latitude_matrix[track[i][0]][track[i][1]],
                              longitude_matrix[track[i][0]][track[i][1]]])
    print("Latitude & Longitude Coordinate Path :")
    print(lat_long_path)
    print("\n")
    ans["anticlockwise_path"] = lat_long_path.copy()
    lat_long_path.clear()

    track.clear()

    return ans
