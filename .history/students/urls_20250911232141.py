from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:student_id>/', views.view_student, name='view_student'),
]