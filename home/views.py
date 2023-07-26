from django.shortcuts import render
from django.http import HttpResponse

# Create functions here
# Create your views here.
def home(request):
    return HttpResponse('Hello, world')