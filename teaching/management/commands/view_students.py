from django.contrib.auth.models import User
from django.core.management import BaseCommand

from teaching.models import Teacher


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(username='vayom')
        teacher, created = Teacher.objects.get_or_create(user=user)
        students = teacher.students.all()
        for student in students:
            print(student)
        print(students)
