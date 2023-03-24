from django.shortcuts import render
from .models import Idee
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserCreationFormCustom
from django.contrib.auth.decorators import login_required

# Create your views here.
def about(request):
    return render(request, 'main/about.html')

def home(request):
    return render(request, 'main/home.html')

   
@login_required
def page_idee(request):

    idees = Idee.objects.all() #recuperer tt les ideesd e ma BDD

    return render(request,'main/page_idee.html', {'liste_idees': idees})


class SignupPage(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    form_class = UserCreationFormCustom
    
def login(request):
    return render(request,'registration/login.html')