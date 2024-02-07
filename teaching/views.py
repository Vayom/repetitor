from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DeleteView, ListView

from teaching.models import Teacher, Student


def home(request: HttpRequest):
    user = request.user
    if user.is_authenticated:
        teacher = Teacher.objects.filter(user=user)
        student = Student.objects.filter(user=user)
        context = {
            'teacher': teacher,
            'student': student,
            'user': user,
        }
        return render(request, 'teaching/home.html', context)
    return render(request, 'teaching/home.html', context={})


def create_teacher(request: HttpRequest):
    teacher = Teacher.objects.create(user=request.user)
    return redirect(reverse('home'))


def create_student(request: HttpRequest):
    student = Student.objects.create(user=request.user)
    return redirect(reverse('home'))


def delete_teacher(request: HttpRequest):
    teacher = Teacher.objects.filter(user=request.user).delete()
    return redirect(reverse('home'))


class TeacherConfirmDeleteView(TemplateView):
    template_name = 'teaching/teacher_confirm_delete.html'


def delete_student(request: HttpRequest):
    student = Student.objects.filter(user=request.user).delete()
    return redirect(reverse('home'))


class StudentConfirmDeleteView(TemplateView):
    template_name = 'teaching/student_confirm_delete.html'


def teachers_list(request: HttpRequest):
    # TODO optimize ORM in this view
    teachers = Teacher.objects.prefetch_related('students_request').all()
    student = Student.objects.get(user=request.user)
    context = {
        'teachers': teachers,
        'student': student
    }
    template_name = 'teaching/teacher_list.html'
    return render(request, template_name, context)


def send_request(request: HttpRequest, teacher_id: int):
    user = request.user
    student = Student.objects.get(user=user)
    teacher = Teacher.objects.get(pk=teacher_id)
    teacher.students_request.add(student)
    teacher.save()
    return redirect(reverse('teaching:teacher_list'))


def view_requests(request: HttpRequest):
    # TODO optimize ORM in this view
    teacher = Teacher.objects.get(user=request.user)
    return render(request, 'teaching/view_requests.html', {'teacher': teacher})


def accept_request(request: HttpRequest, student_id: int):
    teacher = Teacher.objects.get(user=request.user)
    student = Student.objects.get(pk=student_id)
    teacher.students.add(student)
    teacher.students_request.remove(student)
    teacher.save()
    return redirect(reverse('teaching:view_requests'))


