from django import forms
from .models import Student,Lecturer,Admin,Department,Attendance,Subject

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

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subjectCode', 'subjectName', 'D_Code']

class UpdateMarksForm(forms.Form):
    student_id = forms.CharField(max_length=9, label='Student Number')  # Ensure this matches your DB length
    assessment_code = forms.CharField(max_length=225, label='Assessment Code')
    new_marks = forms.IntegerField(label='New Marks')