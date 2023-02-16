"""django_sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from notes.views import home_view, new_note_form
from login.views import signup_view, signin_view, signout_view
from weather.views import weather_view
from wiki.views import wiki_view
from .views import mainpage_view

urlpatterns = [
    path('', mainpage_view),
    path('polls/', include('polls.urls')),
    path('login/', signin_view),
    path('login/signup', signup_view),
    path('login/signout', signout_view),
    path('notes/', home_view),
    path('notes/newnote', new_note_form),
    path('admin/', admin.site.urls),
    path('weather/', weather_view),
    path('wiki/', wiki_view)
]
