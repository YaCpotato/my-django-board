from django.urls import path 
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('program/',views.program_list, name='program_list')
]