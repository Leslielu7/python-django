from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

#Create class-based views here.
class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class HomeView(TemplateView):#inherit the TemplateView
    template_name = 'home/welcome.html'
    extra_context = {'today':datetime.today()}




