from rest_framework import serializers
from sk.models import Student
from sk.models import Professor
from sk.models import Lecture
from sk.models import Chapter
from sk.models import Attendence

class StudentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Student
        fields = (
            'url',
            'pk',
            'Name',
            'Major',
            'Gender',
            'Birth',
            'Age',
            'Description',
            'Created',
        )

class LectureSerializer(serializers.HyperlinkedModelSerializer):

    Student = StudentSerializer(many=True, read_only=True)
    Professor = serializers.SlugRelatedField(queryset=Professor.objects.all(), slug_field='Name')

    class Meta:
        model = Lecture
        fields = (
            'url',
            'Student',
            'Professor',
            'Name',
            'Description',
            'Max_chapter',
            'Created',
        )


class ProfessorSerializer(serializers.HyperlinkedModelSerializer):

    Lectures = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='lecture-detail'
    )

    class Meta:

        model = Professor
        fields = (
            'url',
            'pk',
            'Lectures',
            'Name',
            'Major',
            'Created',
        )


class ChapterSerializer(serializers.HyperlinkedModelSerializer):

    Lecture = serializers.SlugRelatedField(queryset=Lecture.objects.all(), slug_field='Name')

    class Meta:

        model = Chapter
        fields = (
            'url',
            'pk',
            'Lecture',
            'Name',
            'Current_chapter',
            'start_date',
            'end_date',
        )


class AttendenceSerializer(serializers.HyperlinkedModelSerializer):

    Lecture = serializers.SlugRelatedField(queryset=Lecture.objects.all(), slug_field='Name')
    Student = serializers.SlugRelatedField(queryset=Student.objects.all(), slug_field='Name')
    Chapter = serializers.SlugRelatedField(queryset=Chapter.objects.all(), slug_field='Name')


    class Meta:

        model = Attendence
        fields = (
            'url',
            'pk',
            'Lecture',
            'Student',
            'Chapter',
        )
