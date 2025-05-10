from django.db import connection

def update_marks(student_id, assessment_code, new_marks):
    with connection.cursor() as cursor:
        cursor.callproc('update_student_marks', [student_id, assessment_code, new_marks])