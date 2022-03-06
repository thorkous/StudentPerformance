from django import forms
from rest_framework import serializers
from . models import Students, Subjects, SubjectMarks, StudentPercentage

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = [
            'name',
            'email',
            'parent_name',
            'adhar',
            'student_id',
        ]

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = [
            'subject_id',
            'name',
            'description',
        ]
class SubjectMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectMarks
        fields = [
            'subject_id',
            'student_id',
            'student_marks'
        ]

class StudentPercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPercentage
        fields = [
            'student_id',
            'marks',
            'total_subject'
        ]
        depth = 1