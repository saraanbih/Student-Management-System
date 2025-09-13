from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>/', views.view_student, name='view_student'),
    path('add/', views.add, name='add'),
    path('edit/<int:student_id>/', views.edit, name='edit'),
    path('delete/<int:student_id>/', views.delete, name='delete'),

    # login/logout
    path('login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next), name='logout'),
]
