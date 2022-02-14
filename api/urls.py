from django.urls import path
from api.views import Direccion

urlpatterns = [
    path('direccion/', Direccion.as_view(), name="direccion"),
]


