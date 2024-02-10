from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Homework(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    difficulty = models.IntegerField(null=False, default=0)
    teacher = models.ForeignKey('Teacher', null=True, on_delete=models.CASCADE)
    student = models.ForeignKey('Student', blank=True, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.tittle


class UserProfile(models.Model):
    """
        UserProfile table. ONE-TO-ONE relationship with User
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    students = models.ManyToManyField('Student', related_name='students', blank=True)
    students_request = models.ManyToManyField('Student', related_name='students_request', blank=True)

    def __str__(self):
        return f'{self.user.username}'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'

