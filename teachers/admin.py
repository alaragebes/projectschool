from django.contrib import admin
from .models import Teacher


class TeacherAdmin (admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject_area', 'lecture', 'get_lecture_code')

    def get_lecture_code(self, obj):
        if obj.lecture:
            return obj.lecture.lecture_code
        return ""
    get_lecture_code.short_description = "Lecture Code"


admin.site.register(Teacher, TeacherAdmin)
