from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

class SecondHome(TemplateView):
    template_name = 'secondhome.html'

# Create your views here.
