from django.shortcuts import render, get_object_or_404
from .models import Lecture
from .forms import LectureForm
from django.http import HttpResponse
from teachers.models import Teacher
from students.models import Student

def lecture_list (request):
    lectures = Lecture.objects.all()
    return render(request, 'lectures/lecture_list.html', {'lectures' : lectures})

def lecture_detail (request):
    print (request.GET.get('pk'))
    lecture = get_object_or_404(Lecture, id=request.GET.get('pk'))
    return render (request, 'lectures/lecture_detail.html', {'lecture' : lecture})

def lecture_add (request):
    if request.method == 'POST':
        form = LectureForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks, your changes have been saved.')
    else :
        form = LectureForm()
    return render(request, 'lectures/lecture_add.html', {'form' : form})

                                                            
