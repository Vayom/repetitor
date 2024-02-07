from django.contrib import admin

from teaching.models import Homework, Teacher, UserProfile, Student


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'teacher', 'students']


admin.site.register(Teacher)
admin.site.register(UserProfile)
admin.site.register(Student)
