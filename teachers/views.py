from django.shortcuts import render, get_object_or_404
from .models import Teacher
from .forms import TeacherForm
from django.http import HttpResponse


def teacher_list (request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/name.html', {'teachers' : teachers})


def teacher_detail (request):
    print (request.GET.get('pk'))
    teacher = get_object_or_404(Teacher, id=request.GET.get('pk'))
    return render(request, 'teachers/detail.html', {'teacher' : teacher})


def teacher_add (request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks! Your changes have been made.')
    else :
        form = TeacherForm()
    return render(request, 'teachers/add-to-list.html', {'form' : form})
