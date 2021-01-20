from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

class CustomUserCreationFrom(UserCreationForm):
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    email = forms.EmailField(max_length=50)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    gender_choices = (
        ('M','Male'),
        ('F','Female')
    )
    gender = forms.ChoiceField(label='Gender', choices=gender_choices, widget = forms.RadioSelect)
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ('date_of_birth','gender',)

    

class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    email = forms.EmailField(max_length=50)
    class Meta(UserChangeForm):
        model = User
        fields = UserChangeForm.Meta.fields