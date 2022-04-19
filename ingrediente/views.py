from rest_framework import generics, viewsets, filters
from rest_framework.views import APIView
from ingrediente.models import Ingrediente, Receita
from ingrediente.serializers import IngredienteSerializer, ReceitaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class IngredienteViewSet(viewsets.ModelViewSet):
    """Recurso de ingredientes"""
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'categoria']
    pagination_class=None

class ReceitaViewSet(viewsets.ModelViewSet):
    """Recurso de receitas"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'ingredientes']
    pagination_class=None