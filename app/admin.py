from django.contrib import admin
from .models import Student

class StudentModelAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "contact", "address")

admin.site.register(Student, StudentModelAdmin)
