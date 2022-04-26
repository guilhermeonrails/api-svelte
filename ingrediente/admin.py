from django.contrib import admin
from ingrediente.models import Ingrediente, Receita

class Ingredientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria')

admin.site.register(Ingrediente, Ingredientes)

class Receitas(admin.ModelAdmin):
    list_display = ('id', 'nome',)


admin.site.register(Receita, Receitas)