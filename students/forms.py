from django import forms
from .models import Student
from django.core.exceptions import NON_FIELD_ERRORS


class NameForm(forms.Form):
    your_name = forms.CharField(label = 'Your name', max_length = 100)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['parent_name']

        error_messages = {
            NON_FIELD_ERRORS : {'unique_together': "%(model_name)s's %(field_labels)s are not unique."}

        }
