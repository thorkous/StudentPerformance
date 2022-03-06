from django.urls import path
from . import views

from backend.serializers import SubjectMarksSerializer
from backend.models import SubjectMarks


urlpatterns=[
    path('savestudents', views.save_students),
    path('getstudent', views.get_student),
    path('savesubject', views.save_subject),
    path('getsubjects',views.get_subject),
    path('savemarks', views.save_subject_marks),
    path('getmarks', views.get_subject_marks)
]

# def one_time_startup():
#     max_marks = {}
#     object = SubjectMarks.objects.all()
#     serializer = SubjectSerializer(object)
#     for subject in serializer.instance:
#         temp = SubjectSerializer(subject)
#         subject_id = temp.data['subject_id']
#         student_id = temp.data['student_id']
#         marks = temp.data['student_marks']
#         print(subject_id, student_id, marks)
