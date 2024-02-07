from django.contrib.auth.views import LoginView
from django.urls import path

from auth_sys.views import logout_view, RegisterView
from teaching.views import create_teacher, delete_teacher, TeacherConfirmDeleteView, create_student, delete_student, \
    StudentConfirmDeleteView, teachers_list, send_request, view_requests, accept_request

app_name = 'teaching'

urlpatterns = [
    path('teacher/create_teacher/', create_teacher, name='create_teacher'),
    path('teacher/delete_teacher/', delete_teacher, name='delete_teacher'),
    path('teacher/confirm_delete/', TeacherConfirmDeleteView.as_view(), name='teacher_confirm_delete'),
    path('teacher/teacher_list/', teachers_list, name='teacher_list'),
    path('teacher/view_requests/', view_requests, name='view_requests'),
    path('teacher/accept_request/<int:student_id>', accept_request, name='accept_request'),
    path('student/create_student/', create_student, name='create_student'),
    path('student/delete_student/', delete_student, name='delete_student'),
    path('student/confirm_delete/', StudentConfirmDeleteView.as_view(), name='student_confirm_delete'),
    path('student/send_request/<int:teacher_id>', send_request, name='send_request'),

]