from shapely.geometry.polygon import Polygon
from shapely.geometry import Point
from shapely.geometry import LineString
import numpy as np
from osm2geojson import json2geojson
import requests


def get_data_from_overpass(query):
    endpoint = "https://overpass-api.de/api/interpreter"
    response = requests.get(endpoint, params={'data': query})
    overpass_json_data = response.json()
    geojson_data = json2geojson(overpass_json_data)
    return geojson_data

# take a list of polygon coordinates. return a normalized polygon collections and a boundary box


def normalization_of_polygon_collection(polygon_collection, bbox):
    # perform normalization and inversion of default geojson coordiantes
    polygon_collection = list(map(lambda x: list(map(lambda y: [int(round(
        y[1]-bbox[0], 3)*RESOLUTION_FACTOR), int(round(y[0]-bbox[1], 3)*RESOLUTION_FACTOR)], x)), polygon_collection))
    # convert it into shapely polygon objects
    polygon_collection = list(map(lambda p: Polygon(p), polygon_collection))
    return (polygon_collection)


def normalization_of_node_collection(node_collection, bbox):
    node_collection = list(map(lambda x: [int(round(x[1]-bbox[0], 3)*RESOLUTION_FACTOR), int(
        round(x[0]-bbox[1], 3)*RESOLUTION_FACTOR)], node_collection))
    node_collection = list(map(lambda x: Point(x), node_collection))
    return (node_collection)


def noramalizatioin_of_line_collection(line_collection, bbox):
    line_collection = list(map(lambda x: list(map(lambda y: [int(round(
        y[1]-bbox[0], 3)*RESOLUTION_FACTOR), int(round(y[0]-bbox[1], 3)*RESOLUTION_FACTOR)], x)), line_collection))
    line_collection = list(map(lambda x: LineString(x), line_collection))
    return(line_collection)


def normalization_of_custommarker_collection(marker_collection, bbox):
    marker_collection = list(map(lambda x: [int(round(x[0]-bbox[0], 3)*RESOLUTION_FACTOR), int(
        round(x[1]-bbox[1], 3)*RESOLUTION_FACTOR), x[2]], marker_collection))
    marker_collection = list(
        map(lambda x: Point(x[0], x[1]).buffer(0.01*x[2]), marker_collection))
    return(marker_collection)


def get_water_data(BOUNDARY_BOX):
    bbox = f"{BOUNDARY_BOX[0]},{BOUNDARY_BOX[1]},{BOUNDARY_BOX[2]},{BOUNDARY_BOX[3]}"
    water_query = f"[out:json][timeout:100];(way[waterway]({bbox});node[water]({bbox});way['water'='lake']({bbox});way[natural=water]({bbox});relation[natural=water]({bbox}););out body;>;out skel qt;"
    result = get_data_from_overpass(water_query)
    water_polygons = []
    water_lines = []
    for i in result["features"]:
        if i['geometry']['type'] == "LineString":
            water_lines.append(i)
        if(i['geometry']['type'] == "Polygon"):
            water_polygons.append(i)
    return(water_polygons, water_lines)


def get_forest_data(BOUNDARY_BOX):
    bbox = f"{BOUNDARY_BOX[0]},{BOUNDARY_BOX[1]},{BOUNDARY_BOX[2]},{BOUNDARY_BOX[3]}"
    forest_query = f"[out:json][timeout:100];(way['natural'='wood']({bbox});way['landuse'='recreation_ground']({bbox});way['landuse'='meadow']({bbox});way['natural'='scrub']({bbox});way['leisure'='park']({bbox}););out body;>;out skel qt;"
    result = get_data_from_overpass(forest_query)
    forest_polygons = []
    for i in result["features"]:
        if(i['geometry']['type'] == "Polygon"):
            forest_polygons.append(i)
    return(forest_polygons)


def get_node_data(BOUNDARY_BOX):
    bbox = f"{BOUNDARY_BOX[0]},{BOUNDARY_BOX[1]},{BOUNDARY_BOX[2]},{BOUNDARY_BOX[3]}"
    nodes_query = f"[out:json][timeout:100];(node['amenity'='hospital']({bbox});node['amenity'='school']({bbox});node['amenity'='college']({bbox});node['amenity'='university']({bbox}););out body;>;out skel qt;"
    result = get_data_from_overpass(nodes_query)
    node_points = []
    for i in result["features"]:
        if(i['geometry']['type'] == "Point"):
            node_points.append(i)
    return(node_points)


def find_matrix(boundary_box, tags, custom_circles_list):
    print("getting data from api")
    global BOUNDARY_BOX, RESOLUTION_FACTOR, RESOLUTION_DECIMAL
    BOUNDARY_BOX = boundary_box
    RESOLUTION_FACTOR = 1000
    RESOLUTION_DECIMAL = 3
    # BOUNDARY_BOX = [27.1794487823,77.454256286,27.245857,77.526784667]
    try:
        if(tags.get("water", False)):
            (water_polygons, water_lines) = get_water_data(BOUNDARY_BOX)
            water_polygon_collection = list(
                map(lambda x: x["geometry"]["coordinates"][0], water_polygons))
            waterline_collection = list(
                map(lambda x: x["geometry"]["coordinates"], water_lines))
            # converting real world coordinates to normalized coordinates to plot on matrix indexes(index can be [0 to n] and only positive integer)
            water_polygon_list = normalization_of_polygon_collection(
                water_polygon_collection, BOUNDARY_BOX)
            waterline_list = noramalizatioin_of_line_collection(
                waterline_collection, BOUNDARY_BOX)
        if(tags.get("forest", False)):
            forest_polygons = get_forest_data(BOUNDARY_BOX)
            forest_polygon_collection = list(
                map(lambda x: x["geometry"]["coordinates"][0], forest_polygons))
            # converting real world coordinates to normalized coordinates to plot on matrix indexes(index can be [0 to n] and only positive integer)
            forest_polygon_list = normalization_of_polygon_collection(
                forest_polygon_collection, BOUNDARY_BOX)
        if(tags.get("school_hospitals")):
            node_points = get_node_data(BOUNDARY_BOX)
            nodes_collection = list(
                map(lambda x: x["geometry"]["coordinates"], node_points))
            # converting real world coordinates to normalized coordinates to plot on matrix indexes(index can be [0 to n] and only positive integer)
            nodes_list = normalization_of_node_collection(
                nodes_collection, BOUNDARY_BOX)
        custom_markers_list = normalization_of_custommarker_collection(
            custom_circles_list, BOUNDARY_BOX)
    except:
        raise Exception("error in api calls")

    bbox = [0, 0, int((round(BOUNDARY_BOX[2], RESOLUTION_DECIMAL)-round(BOUNDARY_BOX[0], RESOLUTION_DECIMAL))
                      * RESOLUTION_FACTOR), int(round(BOUNDARY_BOX[3]-BOUNDARY_BOX[1], RESOLUTION_DECIMAL)*RESOLUTION_FACTOR)]

    print(bbox, "MATRIX INDICES")
    print("starting matrix formation")

    # creating empty matrix
    matrix = [[{"w": 0, "f": 0, "s_h": 0, "p": 0, "c": 0}
               for _ in range(0, bbox[3])] for _ in range(0, bbox[2])]

    # calculation of lat and longs for normalized cells
    base_lat = round(BOUNDARY_BOX[0], RESOLUTION_DECIMAL)
    base_lng = round(BOUNDARY_BOX[1], RESOLUTION_DECIMAL)

    # filling water in matrix
    if(tags.get("water", False)):
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                point = Point(i, j)
                for polygon in water_polygon_list:
                    if(polygon.covers(point)):
                        matrix[i][j]["w"] = 1
                for line in waterline_list:
                    if(line.distance(point) < 0.5):
                        matrix[i][j]["w"] = 1

    # filling forest in matrix
    if(tags.get("forest", False)):
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                point = Point(i, j)
                for polygon in forest_polygon_list:
                    if(polygon.covers(point)):
                        matrix[i][j]["f"] = 1

    # filling nodes in matrix
    if(tags.get("school_hospitals", False)):
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                point = Point(i, j)
                if(point in nodes_list):
                    matrix[i][j]["s_h"] = 1

    # filling custom markers in matrix
    if(custom_markers_list != []):
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                point = Point(i, j)
                for circle in custom_markers_list:
                    if(circle.covers(point)):
                        matrix[i][j]["c"] = 1

# to convert the matrix objects orientation according to real world map
    matrix.reverse()

# adding real world coordinates (this step should be performed only after the reversing of matrix)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            matrix[i][j]["lat"] = round(
                base_lat + (i+1)*(1/RESOLUTION_FACTOR), RESOLUTION_DECIMAL)
            matrix[i][j]["lon"] = round(
                base_lng + (j+1)*(1/RESOLUTION_FACTOR), RESOLUTION_DECIMAL)

    # use this matrix as final output
    FinalMatrix = matrix
    return FinalMatrix
