from django import forms

from .models import Program,Course,Lesson

class ProgramForm(forms.ModelForm):

    class Meta:
        model = Program
        fields = ('id','name','discription','created_date','updated_date')

class CourseForm(forms.ModelForm):

    class Meta:
        model = Program
        fields = ('id','name','discription','created_date','updated_date')

class LessonForm(forms.ModelForm):

    class Meta:
        model = Program
        fields = ('id','name','discription','is_advanced','created_date','updated_date')