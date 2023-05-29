from django.urls import path
from . import views

#URL Configuration
urlpatterns = [
    path('', views.render_homepage, name='homepage') #We pass a path string and a reference to a function (but not calling a function)
]