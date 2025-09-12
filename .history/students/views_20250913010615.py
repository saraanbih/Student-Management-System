from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })

def view_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/view.html', {
        'student': student
    })

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
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'student': student,
                'success': True
            })
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit.html', {
        'form': form,
        'student': student
    })

def delete(request, student_id):
    if request.method == 'POST':
        student = Student.get(Student, pk=student_id)
        student.delete()