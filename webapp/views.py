from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import View

def index_view(request):
    return render(request, 'index.html')