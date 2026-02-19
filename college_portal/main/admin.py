from django.contrib import admin
from .models import Faculty, Course, Placement, StudentProfile

admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Placement)
admin.site.register(StudentProfile)
