from django.urls import path
from . import views

#URL Configuration
urlpatterns = [
    path('HelloWorld/', views.say_hello) #We pass a path string and a reference to a function (but not calling a function)
]