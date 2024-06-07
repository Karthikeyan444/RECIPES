from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




#
# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = contacts
#         fields = '__all__'

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']














