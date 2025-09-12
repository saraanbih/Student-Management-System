from django.shortcuts import render
from .models import Studnet

# Create your views here.
def index(request):
  return render(request, 'students/index.html', )
