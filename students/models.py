from django.db import models
import datetime
from django.utils import timezone
from lectures.models import Lecture


class Student(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField('date of birth')
    where_from = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 100)
    parent_name = models.CharField(max_length = 100)
    lecture = models.ManyToManyField(Lecture, related_name = "students", blank=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
