from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import PasswordInput

from users.apps import UsersConfig
from shop.models import Customer


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not Customer.objects.filter(email=email).exists():
            raise ValidationError(f'That {email} not found.')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if not Customer.objects.filter(password=password).exists():
            raise ValidationError(f'Password did not match')


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if not email or not password:
            raise forms.ValidationError("Username or password invalid")

        return cleaned_data


class RegisterModelForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Customer
        fields = ('email', 'confirm_password', 'password')

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError(f'This {email} already registered.')
        return email

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')
        if password != confirm_password:
            raise forms.ValidationError(f'Password don\'t match')
        return confirm_password