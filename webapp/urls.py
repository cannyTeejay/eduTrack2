from django.urls import path
from . import views

urlpatterns = [
    #Home url
    path('', views.home, name='home'),
    #Student urls
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create, name='student_create'),
    path('students/update/<str:pk>/', views.student_update, name='student_update'),
    path('students/delete/<str:pk>/', views.student_delete, name='student_delete'),
    #Lecturer urls
    path('lecturers/', views.lecturer_list, name='lecturer_list'),
    path('lecturers/add/', views.lecturer_create, name='lecturer_create'),
    path('lecturers/update/<str:pk>/', views.lecturer_update, name='lecturer_update'),
    path('lecturers/delete/<str:pk>/', views.lecturer_delete, name='lecturer_delete'),
    #Admin Auth routes
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    #Admin urls
    path('admins/', views.admin_list, name='admin_list'),
    path('admins/add/', views.admin_create, name='admin_create'),
    path('admins/update/<int:pk>/', views.admin_update, name='admin_update'),
    path('admins/delete/<int:pk>/', views.admin_delete, name='admin_delete'),
    #Department urls
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.department_create, name='department_create'),
    path('departments/update/<str:pk>/', views.department_update, name='department_update'),
    path('departments/delete/<str:pk>/', views.department_delete, name='department_delete'),
    #Attendance urls
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add/', views.attendance_create, name='attendance_create'),
    path('attendance/update/<int:pk>/', views.attendance_update, name='attendance_update'),
    path('attendance/delete/<int:pk>/', views.attendance_delete, name='attendance_delete'),
    
]
