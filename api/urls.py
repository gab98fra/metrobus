from django.urls import path
from api.utils import Direccion
from api.views import ListaUnidades, ListaAlcaldia, MensajeMovilView

urlpatterns = [

    #path('direccion/', Direccion.as_view(), name="direccion"),
    #path('unidades/', ListaUnidades.as_view(), name="unidades"),
    #path('alcaldia/', ListaAlcaldia.as_view(), name="alcaldia"),
    path('mensaje/', MensajeMovilView.as_view(), name="mensaje"),
]


