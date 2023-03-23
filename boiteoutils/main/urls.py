from django.urls import path
from . import views

app_name = "main"





urlpatterns = [
    path('hello/',views.hello),
    path('',views.acceuil),
    path('signup/', views.SignupPage.as_view(), name='signup'),
    
]
