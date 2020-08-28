from django.contrib import admin

# Register your models here.


from .models import Program,Course,Lesson

admin.site.register(Program)
admin.site.register(Course)
admin.site.register(Lesson)