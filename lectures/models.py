from django.db import models

class Lecture (models.Model):
    lecture_name = models.CharField(max_length=200)
    subject_area = models.CharField(max_length=200)
    lecture_code = models.CharField(max_length=50)

    def __str__ (self):
        return self.lecture_name 
