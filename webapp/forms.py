from django import forms
from .models import Student,Lecturer,Admin,Department,Attendance

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentNumber', 'firstName', 'lastName', 'email']

class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['staffNumber', 'firstName', 'lastName', 'email']

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['firstName', 'lastName', 'email']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['D_Code', 'D_Name']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['studentNumber', 'subjectCode', 'status']