from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserCreationFormCustom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']