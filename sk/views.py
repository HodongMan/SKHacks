from sk.models import Student
from sk.models import Professor
from sk.models import Lecture
from sk.models import Chapter
from sk.models import Attendence
from sk.serializers import StudentSerializer
from sk.serializers import LectureSerializer
from sk.serializers import ProfessorSerializer
from sk.serializers import ChapterSerializer
from sk.serializers import AttendenceSerializer

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


class ProfessorList(generics.ListCreateAPIView):

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    name = 'professor-list'

class ProfessorDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    name = 'professor-detail'

class ChapterList(generics.ListCreateAPIView):

    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    name = 'chapter-list'

class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    name = 'chapter-detail'

class AttendenceList(generics.ListCreateAPIView):

    queryset = Attendence.objects.all()
    serializer_class = AttendenceSerializer
    name = 'attendence-list'

class AttendenceDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Attendence.objects.all()
    serializer_class = AttendenceSerializer
    name = 'attendence-detail'


