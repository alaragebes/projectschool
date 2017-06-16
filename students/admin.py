from django.contrib import admin
from .models import Student

class StudentAdmin (admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email', 'where_from', 'get_lecture_name')

    def get_lecture_name(self, obj):
        names = ", ".join([p.lecture_name for p in obj.lecture.all()])
        return names
    get_lecture_name.short_description = "lecture Name"

admin.site.register(Student, StudentAdmin)
