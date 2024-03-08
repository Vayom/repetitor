from django.contrib import admin

from teaching.models import Homework, Teacher, UserProfile, Student


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    fields = ['tittle', 'description', 'teacher', 'student', 'completed', 'verified', 'score', 'file']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ['user']


admin.site.register(UserProfile)
admin.site.register(Teacher)
