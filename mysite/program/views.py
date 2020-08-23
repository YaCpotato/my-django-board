from django.shortcuts import render
from django.utils import timezone

# Create your views here.

def program_list(request):
    return render(request, 'program/program_list.html')
