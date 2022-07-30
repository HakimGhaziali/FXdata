from django.shortcuts import render

# Create your views here.
from django.views import generic




class HomePage(generic.TemplateView):

    template_name='pages/home.html'