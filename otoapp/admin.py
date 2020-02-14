from django.contrib import admin
from .models import Student, Course


class Adminstudent(admin.ModelAdmin):
    list_display = ['name', 'email']


class Admincourse(admin.ModelAdmin):
    list_display = ['course', 'fees']


admin.site.register(Student, Adminstudent)
admin.site.register(Course , Admincourse)
