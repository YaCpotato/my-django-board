from django.shortcuts import render
from django.utils import timezone

# Create your views here.

def todo_list(request):
    return render(request, 'todo/todo_list.html')
