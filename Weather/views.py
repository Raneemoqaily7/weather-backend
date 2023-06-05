# from django.shortcuts import render

# Create your views here.
import requests
import folium
import geocoder

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound



from Weather.api.serializers import SearchSerializer
from .models import Search



@api_view (["GET"])

def get_by_country(req ,country):
    if req.method =="GET":
       
        url = f"https://api.weatherapi.com/v1/current.json?key=3858ed70819a46d0944150122233105&q={country}"

        response = requests.request("GET" ,url)
        return Response (response.json())

        # return Response (response.json()["current"]["temp_c"])

@api_view(["POST"])
def add_country(request):
    if request.method=="POST":
        serializer =SearchSerializer(data =request.data)
        if serializer.is_valid() :
            serializer.save()

            return Response (serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.error , status =status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_countries(request):
    if request.method =="GET":
        url = "https://restcountries.com/v3.1/all"
        response =requests.request("GET" ,url)
        countries =response.json()
        country_names = [country['name']['common'] for country in countries]
        return Response(country_names)
    return Response( status =status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def index(request):
    # Create a folium map
    address =Search.objects.all().last()
    location =geocoder.osm(address)
    country = location.country
    lat= location.lat
    lon=location.lng
    print (country ,"country")
    print (lat,"lat")
    print (lon ,"lng")
    if lat ==None or lon==None:
         address =Search.objects.all().last()
         address.delete()
         return Response ( "not valid")
    map = folium.Map(location=[19,-12],zoom_start=2)
#     html = '''1st line<br>
# 2nd line<br>
# 3rd line'''
    # iframe = folium.IFrame(html,
    #                    width=100,
    #                    height=100)

    # popup = folium.Popup(iframe,
    #                  max_width=100)

    # folium.Marker([43.775, 11.254],
    #                    popup=popup,tooltip="click for more").add_to(map)
    
    
    
    url = f"https://api.weatherapi.com/v1/current.json?key=3858ed70819a46d0944150122233105&q={lat},{lon}"

    response = requests.request("GET" ,url)
    
    folium.Marker([lat,lon],
                       popup=(country ,response.json()["current"]["temp_c"]),tooltip="click for more").add_to(map)
    map_html = map._repr_html_()
    data = {"map": map_html,"lat":lat ,"lng":lon ,"country":country ,"res":response.json()}
    # response = Response (response.json())
    
    
    # Return the response
    return Response(data)