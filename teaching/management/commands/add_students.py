from django.contrib.auth.models import User
from django.core.management import BaseCommand

from teaching.models import Teacher, Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Adding students")
        user1, _ = User.objects.get_or_create(username="hihihi")
        user2, _ = User.objects.get_or_create(username="hohoho")
        user3, _ = User.objects.get_or_create(username="hehehe")
        user4 = User.objects.get(username="vayom")
        teacher, created = Teacher.objects.get_or_create(user=user4)
        student1, created = Student.objects.get_or_create(user=user1)
        student2, created = Student.objects.get_or_create(user=user2)
        student3, created = Student.objects.get_or_create(user=user3)
        print(student3)
        print(teacher)
        teacher.students.add(student1, student2, student3)
        self.stdout.write(self.style.SUCCESS('Successfully added students'))
