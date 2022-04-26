from rest_framework import serializers
from ingrediente.models import Ingrediente, Receita

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id','nome', 'categoria',)

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ('id','nome', 'imagem', 'ingredientes',)