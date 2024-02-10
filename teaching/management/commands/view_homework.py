from django.contrib.auth.models import User
from django.core.management import BaseCommand

from teaching.models import Student, Homework


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(username='vayom2')
        student = Student.objects.get(user=user)
        homeworks = Homework.objects.filter(student=student)
        for homework in homeworks:
            print(homework)
