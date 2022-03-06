# Create your views here.
from backend.models import Students, SubjectMarks, Subjects
from backend.serializers import StudentSerializer, SubjectSerializer, SubjectMarksSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

    serializer = SubjectMarksSerializer(data=request.data)
    subject_id = request.data['subject_id']
    marks = request.data['student_marks']
    if subject_id in max_marks:
        max_marks[subject_id] = max(max_marks[subject_id], marks)
    else:
        marks[subject_id] = marks

    if (serializer.is_valid()):
        data = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "data not good"}, status=400)


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
    object = SubjectMarks.objects.filter(subject_id=subject_id).order_by('-check_in')
    if object:
        serializer = SubjectMarksSerializer(object)
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "data not good"}, status=400)




