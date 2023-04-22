from django.urls import path
from soulsit import views as user_views

urlpatterns = [
    path('', user_views.home, name='home'),
]