from django.db import models

# Create your models here.


class Student(models.Model):
    usn = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=25)
    course = models.CharField(max_length=10)
    college = models.CharField(max_length=50)


class Iot(models.Model):
    usn = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=50)
    internal_marks = models.IntegerField()
    external_marks = models.IntegerField()
    total_marks = models.IntegerField()
    result = models.CharField(max_length=1)


class Bda(models.Model):
    usn = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=50)
    internal_marks = models.IntegerField()
    external_marks = models.IntegerField()
    total_marks = models.IntegerField()
    result = models.CharField(max_length=1)


class Sms(models.Model):
    usn = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=50)
    internal_marks = models.IntegerField()
    external_marks = models.IntegerField()
    total_marks = models.IntegerField()
    result = models.CharField(max_length=1)


class Internship(models.Model):
    usn = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=50)
    internal_marks = models.IntegerField()
    external_marks = models.IntegerField()
    total_marks = models.IntegerField()
    result = models.CharField(max_length=1)


class ProjectPhase2(models.Model):
    usn = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=50)
    internal_marks = models.IntegerField()
    external_marks = models.IntegerField()
    total_marks = models.IntegerField()
    result = models.CharField(max_length=1)


class Seminar(models.Model):
    usn = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=50)
    internal_marks = models.IntegerField()
    external_marks = models.IntegerField()
    total_marks = models.IntegerField()
    result = models.CharField(max_length=1)
