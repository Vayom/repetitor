from django.contrib.auth.views import LoginView
from django.urls import path

from auth_sys.views import logout_view, RegisterView
from teaching.views import create_teacher, delete_teacher, TeacherConfirmDeleteView, create_student, delete_student, \
    StudentConfirmDeleteView, teachers_list, send_request, view_requests, accept_request, my_students_list, \
    delete_student_from_teacher, give_homework, confirm_delete_student_from_teacher, my_homework_view, \
    homework_details_view, my_completed_homework_view, students_homework_view, homework_details_for_teacher, \
    reject_request, homework_send_to_verification

app_name = 'teaching'

urlpatterns = [
    path('teacher/create_teacher/', create_teacher, name='create_teacher'),
    path('teacher/delete_teacher/', delete_teacher, name='delete_teacher'),
    path('teacher/confirm_delete/', TeacherConfirmDeleteView.as_view(), name='teacher_confirm_delete'),
    path('teacher/teacher_list/', teachers_list, name='teacher_list'),
    path('teacher/view_requests/', view_requests, name='view_requests'),
    path('teacher/accept_request/<int:student_id>', accept_request, name='accept_request'),
    path('teacher/reject_request/<int:student_id>', reject_request, name='reject_request'),
    path('teacher/my_students', my_students_list, name='my_students'),
    path('teacher/give_homework/<int:student_id>', give_homework, name='give_homework'),
    path('teacher/students_homework_view/', students_homework_view, name='students_homework_view'),
    path('teacher/homework_details_for_teacher/<int:homework_id>', homework_details_for_teacher,
         name='homework_details_for_teacher'),
    path('teacher/delete_student_from_teacher/<int:student_id>', delete_student_from_teacher,
         name='delete_student_from_teacher'),
    path('teacher/confirm_delete_student_from_teacher/<int:student_id>', confirm_delete_student_from_teacher,
         name='confirm_delete_student_from_teacher'),

    path('student/create_student/', create_student, name='create_student'),
    path('student/delete_student/', delete_student, name='delete_student'),
    path('student/confirm_delete/', StudentConfirmDeleteView.as_view(), name='student_confirm_delete'),
    path('student/send_request/<int:teacher_id>', send_request, name='send_request'),
    path('student/my_homework_view/', my_homework_view, name='my_homework_view'),
    path('student/homework_send_to_verification/<int:homework_id>', homework_send_to_verification,
         name='homework_send_to_verification'),
    path('student/my_completed_homework_view/', my_completed_homework_view, name='my_completed_homework_view'),
    path('student/homework_detail_view/<int:homework_id>', homework_details_view, name='homework_detail_view'),

]
