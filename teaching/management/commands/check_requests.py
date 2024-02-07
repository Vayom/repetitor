from django.contrib.auth.models import User
from django.core.management import BaseCommand

from teaching.models import Teacher


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(username='vayom')
        teacher = Teacher.objects.prefetch_related('students').get(user=user)
        print(teacher.students)