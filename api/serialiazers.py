from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from api.models import Metrobusmodel, AlcaldiaModel


class MensajeSerializer(serializers.Serializer):
    "Mensaje examen api movil"
    
    mensaje=serializers.CharField(help_text="id metrobús")
    
    def validate_mensaje(self, value):
        if len(value)<141:
            pass
        else:
            raise serializers.ValidationError("La longitud es mayor a lo aceptado")
        return value


class MetrobusSerializer(ModelSerializer):
    "Lista de unidades"

    class Meta:
        model=Metrobusmodel
        fields="__all__"

class MetrobusConsultarSerializer(serializers.Serializer):
    "Consultar metrobus con su ubicación"
    
    id=serializers.IntegerField(help_text="id metrobús")
    
    def validate_id(self, value):
        if Metrobusmodel.objects.filter(id=value).exists():
            pass
        else:
            raise serializers.ValidationError("No existe un metrobús con el id ingresado, favor de ingresar uno correcto")
        return value


class AlcaldiaSerializer(ModelSerializer):
    "Lista de alcaldias"

    class Meta:
        model=AlcaldiaModel
        fields="__all__"


class AlcaldiaConsultarSerializer(serializers.Serializer):
    id=serializers.IntegerField(help_text="id alcaldia")
    
    def validate_id(self, value):
        if AlcaldiaModel.objects.filter(id=value).exists():
            pass
        else:
            raise serializers.ValidationError("No existe alcaldía con el id ingresado, favor de ingresar uno correcto")
        return value
