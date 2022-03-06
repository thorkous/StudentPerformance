# Create your views here.
from backend.models import Students, SubjectMarks, Subjects, StudentPercentage
from backend.serializers import StudentSerializer, SubjectSerializer, SubjectMarksSerializer, \
    StudentPercentageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

max_marks = {}


@api_view(["POST"])
def save_students(request, *args, **kwargs):
    serializer = StudentSerializer(data=request.data)

    if (serializer.is_valid()):
        data = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "data not good"}, status=400)


@api_view(["GET"])
def get_student(request, *args, **kwargs):
    id = request.data['id']
    # print(id)
    object = Students.objects.get(student_id=id)
    if object:
        serializer = StudentSerializer(object)
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "data not good"}, status=400)


@api_view(["POST"])
def save_subject(request, *args, **kwargs):
    serializer = SubjectSerializer(data=request.data)
    if (serializer.is_valid()):
        data = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "data not good"}, status=400)


@api_view(["GET"])
def get_subject(request, *args, **kwargs):
    object = Subjects.objects.all()
    print(object)
    response = []
    serializer = SubjectSerializer(object)
    for subject in serializer.instance:
        serializer = SubjectSerializer(subject)
        response.append(serializer.data)
        # print(serializer.data)
    if (len(response)):
        return Response(response)
    return Response({"invalid": "data not good"}, status=400)


@api_view(["POST"])
def save_subject_marks(request, *args, **kwargs):
    subject_id = request.data['subject_id']
    student_id = request.data['student_id']
    marks = request.data['student_marks']
    object = SubjectMarks.objects.filter(subject_id=subject_id, student_id=student_id)
    subjectExist = False
    prevMarks = -1
    if (subject_id and student_id and marks):
        if (object.count() != 0):
            prevMarks = SubjectMarks.objects.get(subject_id=subject_id, student_id=student_id)
            prevMarks = SubjectMarksSerializer(prevMarks).data
            prevMarks = prevMarks['student_marks']
            object.update(student_marks=marks)
            subjectExist = True
        else:
            object.create(subject_id=subject_id, student_id=student_id, student_marks=marks)

        studentPercentage = StudentPercentage.objects.filter(student_id=student_id)
        if (studentPercentage.count() != 0):
            studentPercentageVal = StudentPercentage.objects.get(student_id=student_id)
            studentPercentageVal = StudentPercentageSerializer(studentPercentageVal).data
            overallMarks = studentPercentageVal['marks']
            totalSubjects = studentPercentageVal['total_subject']
            if (subjectExist):
                delta = int(marks) - int(prevMarks)
                overallMarks = int(overallMarks) + delta
                percentage = overallMarks / int(totalSubjects)
                studentPercentage.update(marks=overallMarks, percentage=percentage)
            else:
                overallMarks = overallMarks + marks
                totalSubjects += 1
                percentage = overallMarks / totalSubjects
                studentPercentage.update(marks=overallMarks, percentage=percentage)

        else:
            studentPercentage.create(student_id=student_id, marks=marks, total_subject=1, percentage=int(marks) / 1)

        return Response("Updated")
    else:
        Response({"invalid": "data not good"}, status=400)


@api_view(["GET"])
def get_subject_marks(request, *args, **kwargs):
    subject_id = request.data['subject_id']
    student_id = request.data['student_id']
    object = SubjectMarks.objects.get(subject_id=subject_id, student_id=student_id)
    if object:
        serializer = SubjectMarksSerializer(object)
        print(serializer.data)
        return Response(serializer.data)

    return Response({"invalid": "data not good"}, status=400)


@api_view(["GET"])
def get_max_marks_by_subject(request, *args, **kwargs):
    subject_id = request.data['subject_id']
    if (subject_id in max_marks):
        return Response(max_marks[subject_id])
    else:
        object = SubjectMarks.objects.filter(subject_id=subject_id).order_by('student_marks').last()
        if object:
            serializer = SubjectMarksSerializer(object)
            print(serializer.data)
            max_marks[subject_id] = serializer.data
            return Response(serializer.data)
    return Response({"invalid": "data not good"}, status=400)


@api_view(["GET"])
def get_max_percentage(request, *args, **kwargs):
    subject = StudentPercentage.objects.order_by('percentage').last()
    if subject:
        subject = StudentPercentageSerializer(subject)
        print(subject.data)
        return Response(subject.data['percentage'])
