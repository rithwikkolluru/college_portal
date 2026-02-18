from django.db import models

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
        return str(self.year)


class StudentRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
