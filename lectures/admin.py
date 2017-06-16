from django.contrib import admin
from .models import Lecture

class LectureAdmin(admin.ModelAdmin):
    list_display = ('lecture_name', 'subject_area', 'lecture_code')
    list_display_link = ('lecture_name')

admin.site.register(Lecture, LectureAdmin)
