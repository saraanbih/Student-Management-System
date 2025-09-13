from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Student
from .forms import StudentForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'students/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})

@login_required(login_url='login')
def view_student(request, student_id):
  return HttpResponseRedirect(reverse('index'))

@login_required(login_url='login')
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

@login_required(login_url='login')
def edit(request, student_id):
  if request.method == 'POST':
    student = Student.objects.get(pk=student_id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=student_id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form,
    'student': student
  })

@login_required(login_url='login')
def delete(request, student_id):
  if request.method == 'POST':
    student = Student.objects.get(pk=student_id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
]