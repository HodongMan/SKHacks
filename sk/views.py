from sk.models import Student
from sk.models import Professor
from sk.models import Lecture
from sk.models import Chapter
from sk.models import Attendence
from sk.serializers import StudentSerializer
from sk.serializers import LectureSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

class StudentList(generics.ListCreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    name = 'student-list'

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    name = 'student-detail'

class LectureList(generics.ListCreateAPIView):

    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    name = 'lecture-list'

class LectureDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    name = 'lecture-detail'
