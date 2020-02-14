from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    course = models.CharField(max_length=100)
    fees = models.IntegerField()

    def __str__(self):
        return self.course




