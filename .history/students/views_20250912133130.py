from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all()
  })

def view_student(request, student_id):
  student = Student.objects.get(pk=student_id)
  return HttpResponseRedirect(reverse('index'))

def add(request):
  if request.method != 'POST':
    form = StudentForm(re)
  else:
    form = StudentForm(data=request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('index'))
  
  return render(request, 'students/add.html', {
    'form': form
  })
