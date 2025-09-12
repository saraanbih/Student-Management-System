from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Student
from .forms import StudentForm

def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })

def view_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),  
                'success': True
            })
    else:
        form = StudentForm()

    return render(request, 'students/add.html', {
        'form': form
    })

def edit(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(pk=student_id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect(request,'students/add.html',{
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=student_id)
        form = StudentForm(instance=student)
      