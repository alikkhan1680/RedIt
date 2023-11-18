from django import forms
from .models import ContactModel, Message, User
from django.contrib.auth.forms import UserCreationForm


class ContactForms(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                'rows': '7',
                'cols': '30',

            })
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message', 'parent']
        widgets = {
            'message': forms.Textarea(attrs={
                'id': 'name',
                'class': 'form-control',
            })
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'type': 'password'
            }),

        }


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Enter your password'
        }))
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Confirm your password'
        }))

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'avatar',
                  'bio',
                  'email',
                  'password1',
                  'password2',
                  'avatar']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Bio'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'
            }),

        }
