from django.shortcuts import render
from .models import Idee

# Create your views here.
def hello(request):
    return render(request, 'hello_world.html')


def acceuil(request):

    idees = Idee.objects.all() #recuperer tt les ideesd e ma BDD

    return render(request,'accueil.html', {'liste_idees': idees})