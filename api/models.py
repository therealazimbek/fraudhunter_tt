from django.db import models


class Employee(models.Model):
    firstname = models.CharField(max_length=200, blank=False)
    middlename = models.CharField(max_length=200, blank=False)
    lastname = models.CharField(max_length=200, blank=False)
    position = models.CharField(max_length=200, blank=False)
    joined_date = models.DateTimeField(auto_now_add=True)
    salary = models.PositiveIntegerField(blank=False)
    supervisor = models.ForeignKey('self', on_delete=models.CASCADE)

