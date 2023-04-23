from django.urls import path
from django.contrib.auth import views as auth
from soulsit import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_project/', views.createproject, name="create_project"),
    path('login/', views.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='main.html'), name ='logout'),
    path('register/', views.register, name ='register'),
    path('profile/', views.profile, name='profile'),
    path('projects/', views.project, name='projects'),
    ]