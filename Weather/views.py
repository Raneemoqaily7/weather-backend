# from django.shortcuts import render

# Create your views here.
import requests
import folium
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view (["GET"])

def get_by_country(req ,country):
    if req.method =="GET":
       
        url = f"https://api.weatherapi.com/v1/current.json?key=3858ed70819a46d0944150122233105&q={country}"

        response = requests.request("GET" ,url)
        return Response (response.json())

        # return Response (response.json()["current"]["temp_c"])


@api_view(['GET'])
def index(request):
    # Create a folium map
    map = folium.Map(location=[19,-12],zoom_start=2)
    map_html = map._repr_html_()
    
    # Construct the response data
    data = {"map": map_html}
    
    # Return the response
    return Response(data)