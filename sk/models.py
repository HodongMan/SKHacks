from django.db import models


class Student(models.Model):

    MALE='M'
    FEMALE='F'
    GENDER_CHOICES= (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    Name = models.CharField(max_length=200)
    Major = models.CharField(max_length=200, blank=True, default='')
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Birth = models.DateField()
    Age = models.IntegerField()
    Description = models.TextField()
    Created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('Created',)

    def __str__(self):
        return self.Name

class Professor(models.Model):

    Name = models.CharField(max_length=200)
    Major = models.CharField(max_length=200)
    Created = models.DateTimeField(auto_now_add=True)

class Lecture(models.Model):

    Professor = models.ForeignKey(
        Professor,
        related_name='Lectures',
        on_delete=models.CASCADE
    )
    Student = models.ManyToManyField(Student)
    Name = models.CharField(max_length=200)
    Description = models.TextField()
    Max_chapter = models.IntegerField()
    Created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('Created',)

class Chapter(models.Model):

    Lecture = models.ForeignKey(
        Lecture,
        related_name='Chapters',
        on_delete=models.CASCADE
    )

    Current_chapter = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Attendence(models.Model):

    Chapter = models.ForeignKey(
        Chapter,
        related_name='Chapters',
        on_delete=models.CASCADE
    )
    Student = models.ForeignKey(
        Student,
        related_name='Students',
        on_delete=models.CASCADE
    )
    Lecture = models.ForeignKey(
        Lecture,
        related_name='Lectuers',
        on_delete=models.CASCADE
    )
