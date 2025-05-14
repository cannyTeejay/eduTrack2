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
    student_id = forms.CharField(max_length=9, label='Student Number')
    assessment_code = forms.CharField(max_length=225, label='Assessment Code')
    new_marks = forms.IntegerField(label='New Marks')

class StudentAttendanceForm(forms.Form):
    student_id = forms.CharField(max_length=9, label='Student Number')
    subject_code = forms.CharField(max_length=20, label='Subject Code')

class LecturerSubjectsForm(forms.Form):
    lecturer_id = forms.CharField(max_length=9, label='Lecturer Staff Number')


class RoleLoginForm(forms.Form):
    user_number = forms.CharField(
        label='User Number',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=[
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
        ('admin', 'Admin'),
    ])

    def clean_user_number(self):
        user_number = self.cleaned_data.get('user_number')
        if not user_number:
            raise forms.ValidationError("User number is required.")
        if not user_number.isdigit():
            raise forms.ValidationError("User number must be numeric.")
        return user_number