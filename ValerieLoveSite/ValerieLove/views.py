from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# requests -> response
# request handler
# action

def render_homepage(request):
    return render(request, 'home.html') #TODO: Figure out what context is supposed to go here
