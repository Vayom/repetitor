from rest_framework import serializers
from teaching.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Teacher
        fields = ('id', 'user', 'students')