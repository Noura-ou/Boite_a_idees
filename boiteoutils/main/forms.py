from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .models import Idee

class UserCreationFormCustom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']





class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idee
        fields = ('formulation', 'detail')