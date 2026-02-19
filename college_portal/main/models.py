from django.db import models
from django.contrib.auth.models import User


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='faculty_images/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    rating = models.FloatField()
    image = models.ImageField(upload_to='course_images/')
    description = models.TextField()

    def __str__(self):
        return self.title


class Placement(models.Model):
    year = models.IntegerField()
    percentage = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return f"{self.year} - {self.percentage}%"


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class StudentRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course.title}"

