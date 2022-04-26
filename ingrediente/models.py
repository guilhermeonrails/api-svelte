from django.db import models

class Ingrediente(models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    nome = models.CharField(max_length=50)
    ingredientes = models.ManyToManyField(Ingrediente, blank=True, related_name="ingrediente_id")
    imagem = models.ImageField(blank=True)

    def __str__(self):
        return self.nome