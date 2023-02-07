from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    objects = models.Manager()


class Departments(models.Model):
    dept_id = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    objects = models.Manager()
