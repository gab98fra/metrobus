from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from api.models import Metrobusmodel, AlcaldiaModel

class MetrobusSerializer(ModelSerializer):
    """Lista de unidades metrobús
        
        :param:ModelSerializer serializador referencia para modelos
    """

    class Meta:
        model=Metrobusmodel
        fields="__all__"

class MetrobusConsultarSerializer(serializers.Serializer):
    """Consultar metrobus con su ubicación
        
        :param: Serializer serializador
    """
    
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
    "Serializado para consultar unidades de metrobús por alcadía"
    
    id=serializers.IntegerField(help_text="id alcaldia")
    
    def validate_id(self, value):
        if AlcaldiaModel.objects.filter(id=value).exists():
            pass
        else:
            raise serializers.ValidationError("No existe alcaldía con el id ingresado, favor de ingresar uno correcto")
        return value
