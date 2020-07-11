from matplotlib import pyplot as plt
import math


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


def update_trap():
    global traps
    traps = [[0 for i in range(y_len)] for j in range(x_len)]


def clear_block(start_x, start_y, end_x, end_y):
    water_matrix[start_x][start_y] = 1
    forest_matrix[start_x][start_y] = 1
    population_matrix[start_x][start_y] = 0
    building_matrix[start_x][start_y] = 0

    water_matrix[end_x][end_y] = 1
    forest_matrix[end_x][end_y] = 1
    population_matrix[end_x][end_y] = 0
    building_matrix[end_x][end_y] = 0


def next_cell_selection_from_source_clockwise(source_x, source_y, end_x, end_y):
    '''Clockwise direction follows'''
    possible_steps, distance_list = [], []
    try:
        coordinates = []
        if (water_matrix[source_x-1][source_y] == 1 or forest_matrix[source_x-1][source_y] == 1 or population_matrix[source_x-1][source_y] <= threshold_population) and building_matrix[source_x-1][source_y] == 0 and traps[source_x-1][source_y] == 0:
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
                population_matrix[source_x - 1][source_y+1] <= threshold_population) and building_matrix[source_x - 1][source_y+1] == 0 and traps[source_x - 1][source_y+1] == 0:
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
                population_matrix[source_x][source_y+1] <= threshold_population) and building_matrix[source_x][source_y+1] == 0 and traps[source_x][source_y+1] == 0:
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
                population_matrix[source_x+1][source_y+1] <= threshold_population) and building_matrix[source_x+1][source_y+1] == 0 and traps[source_x+1][source_y+1] == 0:
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
                population_matrix[source_x+1][source_y] <= threshold_population) and building_matrix[source_x+1][source_y] == 0 and traps[source_x+1][source_y] == 0:
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
                population_matrix[source_x+1][source_y-1] <= threshold_population) and building_matrix[source_x+1][source_y-1] == 0 and traps[source_x+1][source_y-1] == 0:
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
                population_matrix[source_x][source_y-1] <= threshold_population) and building_matrix[source_x][source_y-1] == 0 and traps[source_x][source_y-1] == 0:
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
                population_matrix[source_x-1][source_y-1] <= threshold_population) and building_matrix[source_x-1][source_y-1] == 0 and traps[source_x-1][source_y-1] == 0:
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


def next_cell_selection_from_source_anti_clockwise(source_x, source_y, end_x, end_y):
    '''Anti-Clockwise direction follows'''
    possible_steps, distance_list = [], []
    try:
        coordinates = []
        if (water_matrix[source_x-1][source_y-1] == 1 or forest_matrix[source_x-1][source_y-1] == 1 or
                population_matrix[source_x-1][source_y-1] <= threshold_population) and building_matrix[source_x-1][source_y-1] == 0 and traps[source_x-1][source_y-1] == 0:
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
                population_matrix[source_x][source_y-1] <= threshold_population) and building_matrix[source_x][source_y-1] == 0 and traps[source_x][source_y-1] == 0:
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
                population_matrix[source_x+1][source_y-1] <= threshold_population) and building_matrix[source_x+1][source_y-1] == 0 and traps[source_x+1][source_y-1] == 0:
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
                population_matrix[source_x+1][source_y] <= threshold_population) and building_matrix[source_x+1][source_y] == 0 and traps[source_x+1][source_y] == 0:
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
                population_matrix[source_x+1][source_y+1] <= threshold_population) and building_matrix[source_x+1][source_y+1] == 0 and traps[source_x+1][source_y+1] == 0:
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
                population_matrix[source_x][source_y+1] <= threshold_population) and building_matrix[source_x][source_y+1] == 0 and traps[source_x][source_y+1] == 0:
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
                population_matrix[source_x - 1][source_y+1] <= threshold_population) and building_matrix[source_x - 1][source_y+1] == 0 and traps[source_x - 1][source_y+1] == 0:
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
        if (water_matrix[source_x-1][source_y] == 1 or forest_matrix[source_x-1][source_y] == 1 or population_matrix[source_x-1][source_y] <= threshold_population) and building_matrix[source_x-1][source_y] == 0 and traps[source_x-1][source_y] == 0:
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

    return possible_steps, distance_list


def source_to_destination_clockwise(start_x, start_y, end_x, end_y):
    update_trap()
    clear_block(start_x, start_y, end_x, end_y)
    track = [[start_x, start_y]]
    response = True
    temp_source_x, temp_source_y = start_x, start_y
    temp_destination_x, temp_destination_y = end_x, end_y

    distance = 0
    if type_of_distance:
        distance = euclid(temp_source_x, temp_source_y,
                          temp_destination_x, temp_destination_y)
    else:
        distance = manhattan(temp_source_x, temp_source_y,
                             temp_destination_x, temp_destination_y)
    while distance > 0:
        if temp_source_x == temp_destination_x and temp_source_y == temp_destination_y:
            distance = 0
        else:
            possible_steps, possible_distance = next_cell_selection_from_source_clockwise(
                temp_source_x, temp_source_y, temp_destination_x, temp_destination_y)
            possible_distance.sort()
            if len(possible_steps) == 0:
                response = False
                break
            for i in possible_steps:
                if possible_distance[0] == i[2]:
                    if [i[0], i[1]] in track:
                        traps[i[0]][i[1]] = 1
                        temp_source_x, temp_source_y = start_x, start_y
                        track.clear()
                        track.append([start_x, start_y])
                        break
                    else:
                        track.append([i[0], i[1]])
                        temp_source_x, temp_source_y = i[0], i[1]
                        break
    return total_distance(track), track, response


def source_to_destination_anti_clockwise(start_x, start_y, end_x, end_y):
    update_trap()
    clear_block(start_x, start_y, end_x, end_y)
    track = [[start_x, start_y]]
    response = True
    temp_source_x, temp_source_y = start_x, start_y
    temp_destination_x, temp_destination_y = end_x, end_y

    distance = 0
    if type_of_distance:
        distance = euclid(temp_source_x, temp_source_y,
                          temp_destination_x, temp_destination_y)
    else:
        distance = manhattan(temp_source_x, temp_source_y,
                             temp_destination_x, temp_destination_y)
    while distance > 0:
        if temp_source_x == temp_destination_x and temp_source_y == temp_destination_y:
            distance = 0
        else:
            possible_steps, possible_distance = next_cell_selection_from_source_anti_clockwise(
                temp_source_x, temp_source_y, temp_destination_x, temp_destination_y)
            possible_distance.sort()
            if len(possible_steps) == 0:
                response = False
                break
            for i in possible_steps:
                if possible_distance[0] == i[2]:
                    if [i[0], i[1]] in track:
                        traps[i[0]][i[1]] = 1
                        temp_source_x, temp_source_y = start_x, start_y
                        track.clear()
                        track.append([start_x, start_y])
                        break
                    else:
                        track.append([i[0], i[1]])
                        temp_source_x, temp_source_y = i[0], i[1]
                        break

    return total_distance(track), track, response


def shortest_path(start_x, start_y, end_x, end_y):
    final_distance, final_path = [], []

    distance, path, response = source_to_destination_clockwise(
        start_x, start_y, end_x, end_y)
    if response:
        final_distance.append(distance)
        final_path.append(path)

    distance, path, response = source_to_destination_anti_clockwise(
        start_x, start_y, end_x, end_y)
    if response:
        final_distance.append(distance)
        final_path.append(path)

    distance, path, response = source_to_destination_clockwise(
        end_x, end_y, start_x, start_y)
    if response:
        final_distance.append(distance)
        path.reverse()
        final_path.append(path)

    distance, path, response = source_to_destination_anti_clockwise(
        end_x, end_y, start_x, start_y)
    if response:
        final_distance.append(distance)
        path.reverse()
        final_path.append(path)

    try:
        min_distance = min(final_distance)
        min_path = final_path[final_distance.index(min_distance)]
    except:
        return "No possible path", "No possible path"

    return min_distance, min_path


def optimum_path(start_point, points, final_point):
    current_x, current_y = start_point[0][0], start_point[0][1]
    total_point = start_point

    while len(points) > 0:
        final_distance = []
        for point in points:
            distance, path = shortest_path(
                current_x, current_y, point[0], point[1])
            if distance != "No possible path" or path != "No possible path":
                final_distance.append(distance)
            else:
                print("No possible path")
        if len(final_distance) == 0:
            current_x, current_y = point[0], point[1]
        else:
            sort_distance = min(final_distance)
            sort_point = points[final_distance.index(sort_distance)]
            current_x, current_y = sort_point[0], sort_point[1]
            total_point.append(sort_point)
            points.remove(sort_point)
    total_point.append(final_point)
    return total_point


def get_lat_lon_path(path):
    lat_lon_path = []
    for cell in path:
        node = []
        node.append(latitude_matrix[cell[0]][cell[1]])
        node.append(longitude_matrix[cell[0]][cell[1]])
        lat_lon_path.append(node)
    return lat_lon_path


###################################################################################################
'''Main Function '''
###################################################################################################


def find_shortest_path(matrix, normalized_path_nodes, optimum_bool):
    global output, rows, columns, water_matrix, forest_matrix, population_matrix, building_matrix
    global latitude_matrix, longitude_matrix, traps, threshold_population, type_of_distance
    global start_point, final_point, points, size_of_grid, total_distance_km, total_path, total_distances
    global x_len, y_len
    output = matrix
    ans = {}
    optimum = optimum_bool
    final_path, final_path_lat_lon = [], []
    start_point = normalized_path_nodes[0]
    final_point = normalized_path_nodes[-1]
    points = normalized_path_nodes[1:-1]
    total_distance_km = 0
    total_path, total_distances = [], []
    rows, columns = len(output), len(output[0])
    water_matrix = [[0 for i in range(columns)] for j in range(rows)]
    forest_matrix = [[0 for i in range(columns)] for j in range(rows)]
    population_matrix = [[0 for i in range(columns)] for j in range(rows)]
    building_matrix = [[0 for i in range(columns)] for j in range(rows)]
    latitude_matrix = [[0 for i in range(columns)] for j in range(rows)]
    longitude_matrix = [[0 for i in range(columns)] for j in range(rows)]
    x_len, y_len = len(water_matrix), len(water_matrix[0])
    threshold_population = 0.5  # Threshold Population density
    type_of_distance = True  # True = Euclidean Distance and False = Manhattan Distance
    size_of_grid = 11  # size of grid is the dimension of grid by default it is 11m*11m
    for row in range(0, rows):
        for column in range(0, columns):
            water_matrix[row][column] = output[row][column]['w']
            forest_matrix[row][column] = output[row][column]['f']
            if(output[row][column]['s_h'] == 1 or output[row][column]['c'] == 1):
                building_matrix[row][column] = 1
                plt.scatter(row, column)
            else:
                building_matrix[row][column] = 0
            population_matrix[row][column] = output[row][column]['p']
            latitude_matrix[row][column] = output[row][column]['lat']
            longitude_matrix[row][column] = output[row][column]['lon']
    traps = [[0 for i in range(y_len)] for j in range(x_len)]
    if optimum:
        start_point = normalized_path_nodes[0]
        final_point = normalized_path_nodes[-1]
        points = normalized_path_nodes[1:-1]
        total_points_1 = [start_point]
        total_points_1 = optimum_path(total_points_1, points, final_point)
        total_distance_km_1 = 0
        for i in range(0, len(total_points_1) - 1):
            distance, path = shortest_path(total_points_1[i][0], total_points_1[i][1], total_points_1[i + 1][0],
                                           total_points_1[i + 1][1])
            if distance != "No possible path" or path != "No possible path":
                total_distance_km_1 += distance
            else:
                print("No possible path")
        total_points_2 = [final_point]
        total_points_2 = optimum_path(total_points_2, points, start_point)
        total_distance_km_2 = 0
        for i in range(0, len(total_points_2) - 1):
            distance, path = shortest_path(total_points_2[i][0], total_points_2[i][1], total_points_2[i + 1][0],
                                           total_points_2[i + 1][1])
            if distance != "No possible path" or path != "No possible path":
                total_distance_km_2 += distance
            else:
                print("No possible path")

        if total_distance_km_1 < total_distance_km_2:
            start_point = normalized_path_nodes[0]
            final_point = normalized_path_nodes[-1]
            points = normalized_path_nodes[1:-1]
            total_points = [start_point]
            total_points = optimum_path(total_points, points, final_point)
            for point in total_points:
                plt.scatter(point[1], point[0], s=200)
                p = "(" + str(point[0]) + " , " + str(point[1]) + ")"
                plt.annotate(p, (point[1], point[0]))
            for i in range(0, len(total_points) - 1):
                distance, path = shortest_path(total_points[i][0], total_points[i][1], total_points[i + 1][0],
                                               total_points[i + 1][1])
                if distance != "No possible path" or path != "No possible path":
                    total_distance_km += distance
                    x, y = [], []
                    for i in path:
                        x.append(i[1])
                        y.append(i[0])
                    # plt.plot(x, y)
                else:
                    print("No possible path")
        else:
            start_point = normalized_path_nodes[0]
            final_point = normalized_path_nodes[-1]
            points = normalized_path_nodes[1:-1]
            total_points = [final_point]
            total_points = optimum_path(total_points, points, start_point)

            for point in total_points:
                plt.scatter(point[1], point[0], s=200)
                p = "(" + str(point[0]) + " , " + str(point[1]) + ")"
                plt.annotate(p, (point[1], point[0]))

            for i in range(0, len(total_points) - 1):
                distance, path = shortest_path(total_points[i][0], total_points[i][1], total_points[i + 1][0],
                                               total_points[i + 1][1])
                if distance != "No possible path" or path != "No possible path":
                    total_distance_km += distance
                    x, y = [], []
                    for i in path:
                        x.append(i[1])
                        y.append(i[0])
                    plt.plot(x, y)
                else:
                    print("No possibel path")
                    return {"error": "No possible path"}
            total_points.reverse()
    else:
        start_point = normalized_path_nodes[0]
        final_point = normalized_path_nodes[-1]
        points = normalized_path_nodes[1:-1]
        total_points = [start_point]
        for p in points:
            total_points.append(p)
        total_points.append(final_point)
        for point in total_points:
            plt.scatter(point[1], point[0], s=200)
            p = "(" + str(point[0]) + " , " + str(point[1]) + ")"
            plt.annotate(p, (point[1], point[0]))
        for i in range(0, len(total_points)-1):
            distance, path = shortest_path(
                total_points[i][0], total_points[i][1], total_points[i+1][0], total_points[i+1][1])
            if distance != "No possible path" or path != "No possible path":
                total_distance_km += distance
                x, y = [], []
                for i in path:
                    x.append(i[1])
                    y.append(i[0])
                plt.scatter(x, y)
            else:
                print("No possible path")
                return {"error": "No possible path"}

    for i in range(0, len(total_points)-1):
        point_dis, point_path = shortest_path(
            total_points[i][0], total_points[i][1], total_points[i+1][0], total_points[i+1][1])
        for j in point_path:
            final_path.append(j)

    lat_lon_path = get_lat_lon_path(total_points)
    plt.scatter(list(
        map(lambda x: x[1], final_path)), list(map(lambda x: x[0], final_path)))
    final_path_lat_lon = get_lat_lon_path(final_path)

    print("Total distance", total_distance_km, "units")
    print("\nPath Points Latitude & Longitude")
    # print(lat_lon_path)
    # print("\nTotal Path Points")
    # print(final_path)
    # print("\nPath Points Latitude & Longitude")
    # print(final_path_lat_lon)
    print("\nTotal number of pixels travelled", len(final_path_lat_lon))
    print("point_dis", point_dis)

    ans['final_path'] = final_path_lat_lon
    ans['intermediate_stops'] = lat_lon_path
    plt.show()
    return ans
