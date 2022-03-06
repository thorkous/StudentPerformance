from django.db import models

# Create your models here.
class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=120, null=False)
    email = models.EmailField(max_length = 254, null=False)
    parent_name = models.TextField(blank=True, null=True,default="Parent Name not specified")
    adhar = models.TextField(unique = True, null = False, default= "1")

class Subjects(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=120, unique = True, null=False,default="SubjectName")
    description = models.TextField(max_length=120)

class SubjectMarks(models.Model):
    class Meta:
        unique_together = (('subject_id', 'student_id'),)

    subject_id = models.IntegerField(primary_key=True)
    student_id = models.IntegerField()
    student_marks = models.IntegerField(null=False)
