from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET'])
def home_page(request):
    return Response({"message": "Welcome To Student API!"})


# LIST ALL STUDENTS
@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


# ADD A NEW STUDENT
@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "student added!", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET ONE STUDENT BY ID
@api_view(['GET'])
def get_student(request, id):
    student = get_object_or_404(Student, id=id)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

