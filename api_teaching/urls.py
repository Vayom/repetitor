from django.urls import path

from api_teaching.views import TeacherList, DeleteTeacher

app_name = 'api_teaching'

urlpatterns = [
    path('teacher_list/', TeacherList.as_view(), name='teacher_list'),
    path('teacher_delete/<int:pk>/', DeleteTeacher.as_view(), name='teacher_delete')
]