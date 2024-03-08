from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy

from teaching.models import Student, Teacher


def student_required(view_func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        try:
            student = Student.objects.get(user=user)
        except Student.DoesNotExist:
            student = None
        if student:
            return view_func(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))

    return wrapper


def teacher_required(view_func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        try:
            student = Teacher.objects.get(user=user)
        except Teacher.DoesNotExist:
            student = None
        if student:
            return view_func(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))

    return wrapper
