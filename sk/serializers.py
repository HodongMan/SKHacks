from rest_framework import serializers
from sk.models import Student
from sk.models import Professor
from sk.models import Lecture
from sk.models import Chapter
from sk.models import Attendence

class StudentSerializer(serializers.HyperlinkedModelSerializer):

    Lectures = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='lecture'
    )

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
            'Lectures',
        )

class LectureSerializer(serializers.HyperlinkedModelSerializer):

    students = serializers.SlugRelatedField(queryset=Student.objects.all(), slug_field='Name')

    class Meta:
        model = Lecture
        fields = (
            'url',
            'students',
            'Name',
            'Description',
            'Max_chapter',
            'Created',
        )
