from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView

from teaching.models import UserProfile, Teacher, Student


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


def about_me(request: HttpRequest):
    students = None
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        teacher = None

    if teacher:
        students = teacher.students.all()

    student = Student.objects.filter(user=request.user)
    context = {
        'teacher': teacher,
        'students': students,
        'student': student,
    }
    template_name = 'auth_sys/about_me.html'
    return render(request, template_name, context)


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'auth_sys/register.html'
    success_url = reverse_lazy('auth_sys:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object)
        return response
