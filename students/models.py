from django.db import models
import datetime
from django.utils import timezone

class Student(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField('date of birth')
    where_from = models.CharField(max_length = 200)
    email = models.CharField(max_length = 100)
    parent_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + str(self.date_of_birth) +' ' + self.where_from + ' ' + self.email
