from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student

# Create your views here.
def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all()
  })

