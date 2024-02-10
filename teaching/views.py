from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DeleteView, ListView, DetailView

from teaching.forms import AddHomeworkForm
from teaching.models import Teacher, Student, Homework

from teaching.utils import student_required, teacher_required


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


@student_required
def delete_student(request: HttpRequest):
    student = Student.objects.filter(user=request.user).delete()
    return redirect(reverse('home'))


class StudentConfirmDeleteView(TemplateView):
    template_name = 'teaching/student_confirm_delete.html'


def teachers_list(request: HttpRequest):
    # TODO optimize ORM in this view
    teachers = Teacher.objects.prefetch_related('students_request').all()
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = None
    context = {
        'teachers': teachers,
        'student': student
    }
    template_name = 'teaching/teacher_list.html'
    return render(request, template_name, context)


@student_required
def send_request(request: HttpRequest, teacher_id: int):
    user = request.user
    student = Student.objects.get(user=user)
    teacher = Teacher.objects.get(pk=teacher_id)
    teacher.students_request.add(student)
    teacher.save()
    return redirect(reverse('teaching:teacher_list'))


@teacher_required
def view_requests(request: HttpRequest):
    # TODO optimize ORM in this view
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        teacher = None
    return render(request, 'teaching/view_requests.html', {'teacher': teacher})


@teacher_required
def accept_request(request: HttpRequest, student_id: int):
    teacher = Teacher.objects.get(user=request.user)
    student = Student.objects.get(pk=student_id)
    teacher.students.add(student)
    teacher.students_request.remove(student)
    teacher.save()
    return redirect(reverse('teaching:view_requests'))


def reject_request(request: HttpRequest, student_id: int):
    teacher = Teacher.objects.get(user=request.user)
    student = Student.objects.get(pk=student_id)
    teacher.students_request.remove(student)
    teacher.save()
    return redirect(reverse('teaching:view_requests'))


@teacher_required
def my_students_list(request: HttpRequest):
    teacher = Teacher.objects.get(user=request.user)
    students = teacher.students.all()
    context = {
        'students': students,
    }
    return render(request, 'teaching/my_students_list.html', context)


@teacher_required
def delete_student_from_teacher(request: HttpRequest, student_id: int):
    teacher = Teacher.objects.get(user=request.user)
    student = Student.objects.get(pk=student_id)
    homeworks = Homework.objects.filter(student=student, teacher=teacher)
    homeworks.delete()
    teacher.students.remove(student)
    teacher.save()
    return redirect(reverse('teaching:my_students'))


@teacher_required
def confirm_delete_student_from_teacher(request: HttpRequest, student_id: int):
    teacher = Teacher.objects.get(user=request.user)
    student = Student.objects.get(id=student_id)
    context = {
        'teacher': teacher,
        'student': student,
        'student_id': student_id
    }
    template_name = 'teaching/confirm_delete_student_from_teacher.html'
    return render(request, template_name, context)


@teacher_required
def give_homework(request: HttpRequest, student_id: int):
    teacher = Teacher.objects.get(user=request.user)
    student = Student.objects.get(pk=student_id)
    form = AddHomeworkForm()
    context = {
        'teacher': teacher,
        'student': student,
        'form': form,
    }
    if request.method == 'POST':
        form = AddHomeworkForm(request.POST)
        if form.is_valid():
            tittle = form.cleaned_data['tittle']
            description = form.cleaned_data['description']
            difficulty = form.cleaned_data['difficulty']
            homework = Homework.objects.create(
                tittle=tittle,
                description=description,
                difficulty=difficulty,
                student=student,
                teacher=teacher)
            homework.save()
            return redirect(reverse('home'))
    return render(request, 'teaching/give_homework.html', context)


@student_required
def my_homework_view(request: HttpRequest):
    template_name = 'teaching/my_homework_view.html'
    student = Student.objects.get(user=request.user)
    homeworks = Homework.objects.filter(student=student, completed=False)
    context = {
        'student': student,
        'homeworks': homeworks,
    }
    return render(request=request, template_name=template_name, context=context)


@student_required
def homework_details_view(request: HttpRequest, homework_id: int):
    is_current_student = True
    student = Student.objects.get(user=request.user)
    homework = Homework.objects.get(id=homework_id)
    if student != homework.student:
        is_current_student = False
    template_name = 'teaching/homework_details.html'
    context = {
        'homework': homework,
        'is_current_student': is_current_student,
    }
    return render(request, template_name, context)


@student_required
def homework_send_to_verification(request: HttpRequest, homework_id: int):
    homework = Homework.objects.get(id=homework_id)
    homework.completed = True
    homework.verified = False
    homework.score = 0
    homework.save()
    return redirect(reverse('teaching:my_homework_view'))


@student_required
def my_completed_homework_view(request: HttpRequest):
    student = Student.objects.get(user=request.user)
    homeworks = Homework.objects.filter(student=student, completed=True)
    template_name = 'teaching/my_completed_homework_view.html'
    return render(request, template_name, {'homeworks': homeworks})


@student_required
def students_homework_view(request: HttpRequest):
    template_name = 'teaching/students_homework_view.html'
    teacher = Teacher.objects.get(user=request.user)
    homeworks = Homework.objects.filter(teacher=teacher)
    context = {
        'homeworks': homeworks
    }
    return render(request, template_name, context)


@teacher_required
def homework_details_for_teacher(request: HttpRequest, homework_id: int):
    if request.method == 'POST':
        scores = request.POST['scores']
        if scores == '':
            return HttpResponseBadRequest('<h1>Missing "scores"</h1>')
        template_name = 'teaching/verify_homework.html'
        teacher = Teacher.objects.get(user=request.user)
        homework = Homework.objects.get(id=homework_id)
        student = Student.objects.get(id=homework.student.id)
        if homework.student != student or homework.teacher != teacher:
            is_true_homework = False
            return render(request, template_name, context={'is_true_homework': is_true_homework})
        homework.verified = True
        homework.save()
        return redirect(reverse('teaching:students_homework_view'))
    is_current_teacher = True
    teacher = Teacher.objects.get(user=request.user)
    homework = Homework.objects.get(id=homework_id)
    if teacher != homework.teacher:
        is_current_teacher = False
    template_name = 'teaching/homework_details_for_teacher.html'
    context = {
        'homework': homework,
        'is_current_teacher': is_current_teacher,
    }
    return render(request, template_name, context)
