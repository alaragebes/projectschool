from django.db import models
from django.utils import timezone
import datetime
from lectures.models import Lecture


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject_area = models.CharField(max_length=100)
    where_from = models.CharField(max_length=100)
    date_of_birth = models.DateField('date of birth')
    lecture = models.ForeignKey(Lecture, related_name="teachers", null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name 
