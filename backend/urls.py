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
    path('getmarks', views.get_subject_marks),
    path('getmaxmarks', views.get_max_marks_by_subject)
]