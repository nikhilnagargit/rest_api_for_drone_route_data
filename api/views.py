from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from api.FindMatrixUtility import find_matrix
from api.FindShortestPathUtility import find_shortest_path
import json
# Create your views here.

'''

KOTA

{
"source":[25.136582259755453,75.8163070678711],
"destination":[ 25.186301620540558,75.87741851806639],
"intermediate_stops":[[25.154545,75.84234],[25.15523,75.8616256]],
"buffer_radius_km":1,
"tags":{"flyzone":true,"water":true,"forest":true,"school_hospitals":true,"population":true},
"custom_restriction_markers":[[25.15523,75.8616256,100]],
"optimum_path":true
}
'''


def home(request):
    return render(request, "home.html", {})


class FindPathView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Please make post request with points."}, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        source = request.data.get("source", None)
        destination = request.data.get("destination", None)
        buffer_radius = request.data.get("buffer_radius_km", 0)
        tags = request.data.get("tags")
        custom_restriction_markers = request.data.get(
            "custom_restriction_markers")
        optimum_path = request.data.get("optimum_path")
        # check validity of points
        try:
            # finding boundaries of area for data extraction.
            path_list = request.data.get("intermediate_stops")
            path_nodes = [source]+path_list+[destination]
            minix = 99999
            miniy = 99999
            maxix = -99999
            maxiy = -99999
            for i in path_nodes:
                if(i[0] < minix):
                    minix = i[0]
                if(i[1] < miniy):
                    miniy = i[1]
                if(i[0] > maxix):
                    maxix = i[0]
                if(i[1] > maxiy):
                    maxiy = i[1]
            point1 = [minix, miniy]
            point2 = [maxix, maxiy]
            print(point1, point2)
            # adding buffer radius to rectangle area
            point1[0] -= 0.01*(buffer_radius)
            point1[1] -= 0.01*(buffer_radius)
            point2[0] += 0.01*(buffer_radius)
            point2[1] += 0.01*(buffer_radius)
        except:
            print("problem in input json data.")
            return Response({"error": "problem in input json data or accessing data elements at server."}, status=HTTP_400_BAD_REQUEST)
        boundary_box = point1+point2
        # this returns matrix and points corresponding in matrix normalization.

        matrix, normalized_path_nodes = find_matrix(
            boundary_box, tags, custom_restriction_markers, path_nodes)
        print("raster matrix formation successfull.")
        result_dict = find_shortest_path(
            matrix, normalized_path_nodes, optimum_path)

        return Response(json.dumps(result_dict), status=HTTP_200_OK)
