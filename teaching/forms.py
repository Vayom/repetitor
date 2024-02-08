from django import forms

from teaching.models import Homework


class AddHomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('tittle', 'description', 'difficulty')



