from django.shortcuts import render
from django.utils import timezone

# Create your views here.

def top(request):
    return render(request, 'program/search_header.html')
