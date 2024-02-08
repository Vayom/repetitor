from django.contrib.auth.models import User
from django.core.management import BaseCommand

from teaching.models import Teacher, Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(username='vayom2')
        teacher, created = Teacher.objects.get_or_create(user=user)
        student = Student.objects.get(id=4)
        print(student in teacher.students.all())
        print(teacher.students.all())
        print(student)
