from django.shortcuts import render
from rest_framework import viewsets

from .models import Agencia, Carrito
from .serializers import AgenciaSerializer, CarritoSerializer

# Create your views here.
class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer


class AgenciaViewSet(viewsets.ModelViewSet):
    queryset = Agencia.objects.all()
    serializer_class = AgenciaSerializer