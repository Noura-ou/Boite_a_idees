from django.shortcuts import render
from .models import Idee
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserCreationFormCustom

# Create your views here.
def hello(request):
    return render(request, 'main/hello_world.html')


def acceuil(request):

    idees = Idee.objects.all() #recuperer tt les ideesd e ma BDD

    return render(request,'main/accueil.html', {'liste_idees': idees})


class SignupPage(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    form_class = UserCreationFormCustom
    
def login(request):
    return render(request,'registration/login.html')