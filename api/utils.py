from geopy.geocoders import Nominatim
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from api.models import Metrobusmodel, Direccionmodel, AlcaldiaModel, DireccionCompletaModel

geolocator = Nominatim(user_agent=settings.GOOGLE_API_KEY)

class Direccion(APIView):
    "Permite obtener la dirección de acuerdo a la latitud y longitud proporcionada"

    model=Metrobusmodel

    def get(self, request):

        # Obtiene la dirección de acuerdo a la lalt y long enviada
        for obj in self.model.objects.all():
            
            location = geolocator.reverse(f'{obj.position_latitude}, {obj.position_longitude}') 
            Direccionmodel.objects.create(
                id_metrobus=int(obj.id),
                direccion=str(location)
            )            
        # Separa string limitadas por comas
        for dir in Direccionmodel.objects.all():
            sp=dir.direccion.split(sep=",")
            if len(sp)==7:
                try:
                    dir.alcadia=str(sp[3])
                    dir.save()
                except:
                    pass    
            else:
                try:
                    dir.alcadia=str(sp[2])
                    dir.save()
                except:
                    pass
        
        # Asignación de alcadias a modelo metrobus
        for obj in self.model.objects.all():
            direccion=Direccionmodel.objects.get(id_metrobus=int(obj.id))
            try:
                obj.alcadia=AlcaldiaModel.objects.get(alcaldia=direccion.alcadia)
                obj.save()
            except:
                pass
        
        # Asignación de direccion a modelo metrobus
        for obj in self.model.objects.all():
            direccion=Direccionmodel.objects.get(id_metrobus=int(obj.id))
            try:
                direccion=DireccionCompletaModel.objects.create(direccion=direccion.direccion)
                obj.direccion=direccion
                obj.save()
            except:
                pass
        return Response({"result":1}, status=status.HTTP_200_OK)
