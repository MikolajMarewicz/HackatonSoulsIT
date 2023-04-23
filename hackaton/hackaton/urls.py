"""
URL configuration for hackaton project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')le
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from soulsit import views as user_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('soulsit.urls', 'soulsit'), namespace='soulsit')),


    path('', user_view.home, name='home'),
    path('login/', user_view.Login, name ='login'),
    path('register/', user_view.register, name ='register'),
    path('profile/', user_view.profile, name='profile'),
    path('projects/', user_view.projects, name='projects'),
    path('articlemain/', user_view.articlemain, name='articlemain'),
    path('article1/', user_view.article1, name='article1'),
    path('article2/', user_view.article2, name='article2'),
    path('article3/', user_view.article3, name='article3'),
    path('project/', user_view.project, name="project" ),
    path('badgesmain/', user_view.badgesmain, name="badgesmain" ),
    path('chatbot/', user_view.chatbot, name='chatbot'),
    path('learn', user_view.learn, name='learn')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)