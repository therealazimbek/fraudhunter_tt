from django.db import models


class Employee(models.Model):
    firstname = models.CharField(max_length=200, blank=False)
    middlename = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=200, blank=False)
    position = models.CharField(max_length=50, blank=False)
    joined_date = models.DateField()
    salary = models.PositiveIntegerField(blank=False)
    supervisor = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.firstname + " " + self.lastname + " : " + self.position
