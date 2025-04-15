from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    studentNumber = models.CharField(max_length=9,primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=50,unique=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.studentNumber}"


class Lecturer(models.Model):
    staffNumber = models.CharField(max_length=9,primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=50,unique=True, null=True, blank=True)

    def __str__(self):
        return f"Lecturer: {self.firstName} {self.lastName}"


class Admin(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adminID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=50,unique=True, null=True, blank=True)

    def __str__(self):
        return f"Admin: {self.firstName} {self.lastName}"
    
class UserLogs(models.Model):
    logID = models.AutoField(primary_key=True)
    adminName = models.CharField(max_length=255)
    logDescription = models.CharField(max_length=255)
    dateAndTime = models.DateTimeField(auto_now=True)
    logDetails = models.TextField(max_length=255)

    def __str__(self):
        return f"Logs: {self.adminName} - {self.logDescription}. Time - {self.dateAndTime}"

class Department(models.Model):
    D_Code = models.CharField(max_length=225,primary_key=True)
    D_Name = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.D_Code} ({self.D_Name})"

class Subject(models.Model):
    subjectCode = models.CharField(max_length=255,primary_key=True)
    subjectName = models.CharField(max_length=100)
    D_Code = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subjectCode} ({self.subjectName})"
    
class Attendance(models.Model):
    attendID = models.AutoField(primary_key=True)
    studentNumber = models.CharField(max_length=9)
    subjectCode = models.CharField(max_length=20)
    dateAndTime = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.studentNumber} - ({self.subjectCode})"

class StudentProgress(models.Model):
    studentProgressID = models.AutoField(primary_key=True)
    studentNumber = models.ForeignKey(Student,on_delete=models.CASCADE)
    subjectCode = models.ForeignKey(Subject,on_delete=models.CASCADE)
    grade = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.studentNumber} - ({self.subjectCode}) : {self.grade}"
    
class FaceRecognition(models.Model):
    faceRecognitionID = models.AutoField(primary_key=True)
    studentNumber = models.ForeignKey(Student,on_delete=models.CASCADE)
    faceImg = models.CharField(max_length=220)

    def __str__(self):
        return f"{self.studentNumber} - ({self.faceImg})"

class LecturerCourses(models.Model):
    lecturerCourseID = models.AutoField(primary_key=True)
    staffNumber = models.ForeignKey(Lecturer,on_delete=models.CASCADE)
    subjectCode = models.ForeignKey(Subject,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.staffNumber} ({self.subjectCode})"

class Assessment(models.Model):
    assessmentCode = models.CharField(max_length=225,primary_key=True)
    assessmentName = models.CharField(max_length=225)
    totalMark = models.IntegerField()
    subjectCode = models.ForeignKey(Subject,on_delete=models.CASCADE)
    staffNumber = models.ForeignKey(Lecturer,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.assessmentCode} ({self.assessmentName}) - {self.totalMark}"


class StudentMarks(models.Model):
    studentMarkID = models.AutoField(primary_key=True)
    studentNumber = models.ForeignKey(Student,on_delete=models.CASCADE)
    assessmentCode = models.ForeignKey(Assessment,on_delete=models.CASCADE)
    marksObtained = models.IntegerField()

    def __str__(self):
        return f"{self.studentNumber} - ({self.assessmentCode}): Marks-{self.marksObtained}"
