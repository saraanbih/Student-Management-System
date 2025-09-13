from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('index', views.index, name='index'),
    path('<int:student_id>/', views.view_student, name='view_student'),
    path('add/', views.add, name='add'),
    path('edit/<int:student_id>/', views.edit, name='edit'),
    path('delete/<int:student_id>/', views.delete, name='delete'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
