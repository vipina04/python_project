from django import forms
from django.contrib.auth.forms import UserCreationForm
from exam_app.models import Login, Student, Exams




class LoginRegister(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')



class StudentRegister(forms.ModelForm):
    class Meta:
        model =Student
        fields = ('name', 'email', 'student_class', 'phone_number')



class Exam_add(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Exams
        fields = ('date','subject','standard','time')
