from api.models import Student
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializer import StudentSerializer
# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # def get_queryset(self):
    #     return Student.objects.filter(passby = self.request.user)]
    filterset_fields = ['city']