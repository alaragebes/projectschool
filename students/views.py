from django.shortcuts import render, get_object_or_404
from .models import Student

def student_list (request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students' : students})


def detail (request):
    student = get_object_or_404 (Student)
    return render (request, 'students/detail.html', {'student' : student})
