from django.contrib import admin
from .models import Lecturer,Student,Admin,Subject,UserLogs,Department,Attendance,StudentProgress,FaceRecognition,LecturerCourses,Assessment,StudentMarks

# Register your models here.
admin.site.register((Lecturer,Student,Admin,Subject,UserLogs,Department,Attendance,StudentProgress,FaceRecognition,LecturerCourses,Assessment,StudentMarks))
