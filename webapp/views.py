from django.shortcuts import render, redirect, get_object_or_404
from .models import Student,Lecturer,Admin,Department,Attendance,Subject
from .forms import StudentForm,LecturerForm,AdminForm,DepartmentForm,AttendanceForm,SubjectForm,UpdateMarksForm,RoleLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db import connection
from .utils import update_marks


#Home VIEW
def home(request):
    return render(request, 'home.html')

#Student VIEWS

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})

#Lecturer VIEWS

def lecturer_list(request):
    lecturers = Lecturer.objects.all()
    return render(request, 'lecturers/lecturer_list.html', {'lecturers': lecturers})

def lecturer_create(request):
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lecturer_list')
    else:
        form = LecturerForm()
    return render(request, 'lecturers/lecturer_form.html', {'form': form})

def lecturer_update(request, pk):
    lecturer = get_object_or_404(Lecturer, pk=pk)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=lecturer)
        if form.is_valid():
            form.save()
            return redirect('lecturer_list')
    else:
        form = LecturerForm(instance=lecturer)
    return render(request, 'lecturers/lecturer_form.html', {'form': form})

def lecturer_delete(request, pk):
    lecturer = get_object_or_404(Lecturer, pk=pk)
    if request.method == 'POST':
        lecturer.delete()
        return redirect('lecturer_list')
    return render(request, 'lecturers/lecturer_confirm_delete.html', {'lecturer': lecturer})

#Admin VIEWS

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if username and password:
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_list')  # Redirect to admin dashboard
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request,'Please enter both username and password')

    return render(request, 'admin/login.html')


#@login_required
def admin_logout(request):
    logout(request)
    return redirect('admin_login')

#@login_required
def admin_list(request):
    admins = Admin.objects.all()
    return render(request, 'admin/admin_list.html', {'admins': admins})

#@login_required
def admin_create(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            admin = form.save(commit=False)
            admin.user = request.user
            admin.save()
            return redirect('admin_list')
    else:
        form = AdminForm()
    return render(request, 'admin/admin_form.html', {'form': form})
#@login_required
def admin_update(request, pk):
    admin = get_object_or_404(Admin, pk=pk)
    if request.method == 'POST':
        form = AdminForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
            return redirect('admin_list')
    else:
        form = AdminForm(instance=admin)
    return render(request, 'admin/admin_form.html', {'form': form})

#@login_required
def admin_delete(request, pk):
    admin = get_object_or_404(Admin, pk=pk)
    if request.method == 'POST':
        admin.delete()
        return redirect('admin_list')
    return render(request, 'admin/admin_confirm_delete.html', {'admin': admin})

#Department VIEWS

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department/department_list.html', {'departments': departments})

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'department/department_form.html', {'form': form})

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'department/department_form.html', {'form': form})

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'department/department_confirm_delete.html', {'department': department})

#Attendance VIEWS

def attendance_list(request):
    records = Attendance.objects.all()
    return render(request, 'attendance/attendance_list.html', {'records': records})

def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/attendance_form.html', {'form': form})

def attendance_update(request, pk):
    record = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=record)
    return render(request, 'attendance/attendance_form.html', {'form': form})

def attendance_delete(request, pk):
    record = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('attendance_list')
    return render(request, 'attendance/attendance_confirm_delete.html', {'record': record})

#Subject VIEWS

def subject_list(request):
    subjects = Subject.objects.select_related('D_Code').all()
    return render(request, 'subject/subject_list.html', {'subjects': subjects})

def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'subject/subject_form.html', {'form': form})

def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    form = SubjectForm(request.POST or None, instance=subject)
    if form.is_valid():
        form.save()
        return redirect('subject_list')
    return render(request, 'subject/subject_form.html', {'form': form})

def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'subject/confirm_delete.html', {'subject': subject})

#Update Marks VIEWS
def update_student_marks_view(request):
    if request.method == 'POST':
        form = UpdateMarksForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            assessment_code = form.cleaned_data['assessment_code']
            new_marks = form.cleaned_data['new_marks']

            # Calling the procedure to update marks in the database...
            try:
                update_marks(student_id, assessment_code, new_marks)
                return JsonResponse({'status': 'success', 'message': 'Marks updated successfully.'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': f'Error updating marks: {e}'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form data.'})

    else:
        form = UpdateMarksForm()
        return render(request, 'lecturers/update_marks_form.html', {'form': form})
    
#Student Attendance VIEWS
def get_student_attendance(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        subject_code = request.POST.get('subject_code')

        # Call the stored procedure to fetch the attendance
        with connection.cursor() as cursor:
            cursor.callproc('get_student_attendance', [student_id, subject_code])
            rows = cursor.fetchall()

        if rows:
            attendance_status = rows[0][0]
            context = {'attendance_status': attendance_status}
        else:
            context = {'error': 'No attendance records found for the given student and subject.'}

        return render(request, 'attendance/student_attendance.html', context)

    return render(request, 'attendance/student_attendance_form.html')

@login_required
#Lecturer Subjects VIEWS
def get_lecturer_subjects(request):
    if request.method == 'POST':
        lecturer_id = request.POST.get('lecturer_id')

        # Call the stored procedure to fetch the subjects
        with connection.cursor() as cursor:
            cursor.callproc('get_lecturer_subjects', [lecturer_id])
            rows = cursor.fetchall()

        # Process results
        if rows:
            subjects = [{'subject_code': row[0], 'subject_name': row[1]} for row in rows]
            context = {'subjects': subjects}
        else:
            context = {'error': 'No subjects found for the given lecturer.'}

        return render(request, 'lecturers/lecturer_subjects.html', context)

    return render(request, 'lecturers/lecturer_subjects_form.html')


@login_required
def student_dashboard(request):
    try:
        student = Student.objects.get(user=request.user)

        attendance_subjects = Subject.objects.filter(attendance__studentNumber=student)
        progress_subjects = Subject.objects.filter(studentprogress__studentNumber=student)
        marks_subjects = Subject.objects.filter(
            assessment__studentmarks__studentNumber=student
        )

        all_subjects = (attendance_subjects | progress_subjects | marks_subjects).distinct()

        return render(request, 'students/student_dashboard.html', {
            'student': student,
            'subjects': all_subjects,
        })

    except Student.DoesNotExist:
        return redirect('login')


def role_login(request):
    if request.method == 'POST':
        form = RoleLoginForm(request.POST)
        if form.is_valid():
            user_number = form.cleaned_data['user_number']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            user = None
            if role == 'student':
                try:
                    student = Student.objects.get(studentNumber=user_number)
                    user = authenticate(request, username=student.user.username, password=password)
                except Student.DoesNotExist:
                    user = None
            elif role == 'lecturer':
                try:
                    lecturer = Lecturer.objects.get(staffNumber=user_number)
                    user = authenticate(request, username=lecturer.user.username, password=password)
                except Lecturer.DoesNotExist:
                    user = None
            elif role == 'admin':
                try:
                    admin = Admin.objects.get(email=user_number)
                    user = authenticate(request, username=admin.user.username, password=password)
                except Admin.DoesNotExist:
                    user = None

            if user is not None:
                login(request, user)
                # Redirect based on role
                if role == 'student':
                    return redirect('student_dashboard')
                elif role == 'lecturer':
                    return redirect('lecturer_list')
                elif role == 'admin':
                    return redirect('admin_list')
            else:
                messages.error(request, 'Invalid credentials or user not found.')
    else:
        form = RoleLoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')