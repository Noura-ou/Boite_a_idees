from django.urls import path
from . import views

app_name = "main"





urlpatterns = [
    path('about/',views.hello, name = 'about'),
    path('',views.acceuil, name = 'home'),
    path('signup/', views.SignupPage.as_view(), name='signup'),
    
]
