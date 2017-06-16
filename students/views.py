from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

def student_list (request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students' : students})


def detail (request):
    print(request.GET.get('pk'))
    student = Student.objects.get(id=request.GET.get('pk'))
    return render(request, 'students/detail.html', {'student' : student})

def students_add (request):

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks!')
    else :
        form = StudentForm()

        return render (request, 'students/name.html', {'form' : form})
