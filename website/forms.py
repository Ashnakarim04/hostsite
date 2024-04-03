# from django import forms
# from .models import Students

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Students
#         fields = ['sname', 'email', 'course', 'department', 'semester']  # Customize the fields as needed
from django import forms
from .models import AptitudeTest

class AptitudeTestForm(forms.ModelForm):
    class Meta:
        model = AptitudeTest
        fields = ['title', 'description', 'date_and_time', 'duration_minutes']