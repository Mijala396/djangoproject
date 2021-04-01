from django.db import models
from django.utils import timezone


class Tutor(models.Model):
    tutor_first_name=models.CharField(max_length=30)
    tutor_last_name=models.CharField(max_length=30)
    tutor_username=models.CharField(max_length=30)
    tutor_password=models.CharField(max_length=30)
    tutor_address=models.CharField(max_length=30)
    tutor_gender=models.CharField(max_length=30)
    tutor_contactno=models.IntegerField(default=0)
    tutor_emailaddress=models.CharField(max_length=30, unique=True)
    tutor_qualification=models.CharField(max_length=30)
    tutor_educationalInstitute=models.CharField(max_length=30)
    tutor_chargePerHour=models.IntegerField(default=0)

    def __str__(self):
        return self.tutor_first_name

class Student(models.Model):
    student_first_name=models.CharField(max_length=30)
    student_last_name=models.CharField(max_length=30)
    student_username=models.CharField(max_length=30)
    student_password=models.CharField(max_length=30)
    student_address=models.CharField(max_length=30)
    student_gender=models.CharField(max_length=30)
    student_contactno=models.IntegerField(default=0)
    student_emailaddress=models.CharField(max_length=30)
    student_academicLevel=models.CharField(max_length=30)


class Subject(models.Model):
    tutor = models.ForeignKey(Tutor,on_delete=models.PROTECT) #relationship with tutor table
    subject_name = models.CharField(max_length=30)

class Bill(models.Model):
    Payment_type=models.CharField(max_length=30)
    session_cost=models.IntegerField(default=0)

class Sessions(models.Model):
    student = models.ForeignKey(Student,on_delete=models.PROTECT)
    tutor = models.ForeignKey(Tutor,on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject,on_delete=models.PROTECT)
    bill = models.ForeignKey(Bill,on_delete=models.PROTECT)
    session_date = models.DateField(default=timezone.now().date())
    session_time = models.TimeField(default=timezone.now().time())
    session_duration = models.IntegerField(default=0)

class Ratings(models.Model):
    tutor = models.ForeignKey(Tutor,on_delete=models.PROTECT)
    tutor_ratings = models.CharField(max_length=30)
    tutor_review = models.CharField(max_length=30)

