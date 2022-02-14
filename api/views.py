import requests
from django.shortcuts import render
from geopy.geocoders import Nominatim
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings



class Direccion(APIView):
    "Permite obtener la dirección de acuerdo a la latitud y longitud proporcionada"

    def get(self, request):

        geolocator = Nominatim(user_agent=settings.GOOGLE_API_KEY)
        location = geolocator.reverse("19.31749916, -99.18779755") 
        print(location)
        print(location.raw['address'])
        
        return Response({"result":1}, status=status.HTTP_200_OK)
