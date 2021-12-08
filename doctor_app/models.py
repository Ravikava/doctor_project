from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class Role(models.Model):
    Name = models.CharField(max_length=20)

    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.Name

class Master(models.Model):
    Role = models.ForeignKey(Role, on_delete=models.CASCADE)
    Email = models.EmailField(unique=True, default="")
    Password = models.CharField(max_length=12 , default="")
    IsActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'master'

class Course(models.Model):
    CourseName = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.CourseName

class Subject(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    SubjectName = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.SubjectName

class Student(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=20, default="")
    Mobile = models.CharField(max_length=10, default="")
    Gender = models.CharField(max_length=15,default="")
    Dob = models.DateField(auto_created=True, default=timezone.now) 

    class Meta:
        db_table = 'student'

class Faculty(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=20, default="")
    Mobile = models.CharField(max_length=10, default="")
    Gender = models.CharField(max_length=15,default="")
    Dob = models.DateField(auto_created=True, default=timezone.now) 

    class Meta:
        db_table = 'faculty'