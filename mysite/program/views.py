from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Program

# Create your views here.

def top(request):
    return render(request, 'program/search_header.html')

def program_list(request):
    programs = Program.objects.all().order_by('id')
    return render(request, 'program/program_list.html', {'programs': programs})


def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'program/program_detail.html', {'program': program})
