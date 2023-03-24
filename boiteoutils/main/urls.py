from django.urls import path
from . import views

app_name = "main"



urlpatterns = [
    path('about/',views.about, name = 'about'),
    path('page_idee/',views.page_idee, name = 'page_idee'),
    path('creer_idee/',views.creer_idee, name = 'creer_idee'),
    path('',views.home, name = 'home'),
    path('signup/', views.SignupPage.as_view(), name='signup'),

    
]
