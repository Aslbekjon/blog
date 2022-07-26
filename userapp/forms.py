from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserProfile

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password','placeholder':'Confirm password'}
    ),)
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Confirm password'}
    ),)
    class Meta:
        model = UserProfile
        fields = ['username','email','phone_number','password1','password2']

        widgets = {
            'username':forms.TextInput(attrs={'name':'username', 'class':'form-control'}),
            'email':forms.EmailInput(attrs={'name':'email','class':'form-control','placeholder':'Enter your email'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter phone number'}),
        }

class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ['username','first_name','last_name','email','phone_number','image','birthday','bio','address']

        widgets = {
            'username': forms.TextInput(attrs={'name': 'username', 'class': 'form-control'}),
            'email': forms.EmailInput(
                attrs={'name': 'email', 'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'first_name': forms.TextInput(attrs={'name': 'first_name', 'class': 'form-control','placeholder': 'Enter your First name'}),
            'last_name': forms.TextInput(attrs={'name': 'last_name', 'class': 'form-control','placeholder': 'Enter your Last name'}),
            'image': forms.FileInput(attrs={'name': 'image', 'class': 'form-control','placeholder': 'Enter your picture'}),
            'birthday': forms.DateInput(attrs={'name': 'birthday', 'type':'date', 'class':'form-control'}),
            'bio': forms.TextInput(attrs={'name': 'bio', 'class': 'form-control','placeholder': 'Enter short biography'}),
            'address': forms.TextInput(attrs={'name': 'address', 'class': 'form-control','placeholder': 'Enter your address'}),
        }