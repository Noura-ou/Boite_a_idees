from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# les classes vont créer une base donnée dans SQLITE, en faisant migrate
# fait makemigrations pour afficher la base de donnée auth user

class Idee(models.Model):
    formulation = models.CharField(max_length=100)
    detail = models.CharField(max_length=200, null=True)
   # auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Votant(models.Model):
    votant = models.ForeignKey(User, on_delete=models.CASCADE)
    idee = models.ForeignKey(Idee, on_delete=models.CASCADE)
    type_vote = models.BooleanField()