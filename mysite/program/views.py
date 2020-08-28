from django.shortcuts import render
from django.utils import timezone
from .models import Program

# Create your views here.

def top(request):
    return render(request, 'program/search_header.html')

def program_list(request):
    programs = Program.objects.all().order_by('id')
    return render(request, 'program/program_list.html', {'programs': programs})

