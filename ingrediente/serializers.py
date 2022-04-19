from rest_framework import serializers
from ingrediente.models import Ingrediente, Receita

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'

class ReceitaSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True)
    class Meta:
        model = Receita
        fields = ('nome', 'ingredientes', 'imagem')