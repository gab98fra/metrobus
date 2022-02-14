from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serialiazers import MetrobusSerializer, MetrobusConsultarSerializer, AlcaldiaSerializer, AlcaldiaConsultarSerializer
from api.models import Metrobusmodel, AlcaldiaModel

class ListaUnidades(APIView):
    "Get:Muestra la lista de unidades disponibles, post: consultar la unidad enviando el id"
    
    def get(self, request):

        api=Metrobusmodel.objects.all()
        serializer=MetrobusSerializer(api, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = MetrobusConsultarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        metrobus=Metrobusmodel.objects.get(id=serializer.data.get('id'))
        response={
            "id":metrobus.id,
            "position_latitude":metrobus.position_latitude,
            "position_longitude":metrobus.position_longitude,
            "geographic_point":metrobus.geographic_point,
            "position_speed":metrobus.position_speed,
            "position_odometer":metrobus.position_odometer,
            "dirección completa":metrobus.direccion.direccion
        }
        return Response(response, status=status.HTTP_200_OK)

    def get_serializer(self):
        return MetrobusConsultarSerializer()

class ListaAlcaldia(APIView):
    "Get:Muestra la lista de alcaldías disponibles, post: consultar unidades dentro de la alcaldía"

    def get(self, request):

        api=AlcaldiaModel.objects.all()
        serializer=AlcaldiaSerializer(api, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = AlcaldiaConsultarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        alcaldia=AlcaldiaModel.objects.get(id=serializer.data.get('id'))
        lista=[]
        for metrobus in Metrobusmodel.objects.filter(alcaldia=alcaldia):
            response={
                "id":metrobus.id,
                "position_latitude":metrobus.position_latitude,
                "position_longitude":metrobus.position_longitude,
                "geographic_point":metrobus.geographic_point,
                "position_speed":metrobus.position_speed,
                "position_odometer":metrobus.position_odometer,
                "alcaldia":metrobus.alcaldia.alcaldia,
                "dirección completa":metrobus.direccion.direccion
            }
            lista.append(response)

        return Response({"id_alcaldia": alcaldia.id, "alcadia": alcaldia.alcaldia,"Unidades":lista}, status=status.HTTP_200_OK)
    
    def get_serializer(self):
        return AlcaldiaConsultarSerializer()