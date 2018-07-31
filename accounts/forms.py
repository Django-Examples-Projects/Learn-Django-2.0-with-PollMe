from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    """Registration Form."""
    username = forms.CharField(
                            label='Username', 
                            max_length=100, 
                            min_length=5,
                            widget=forms.TextInput(attrs={'Class': 'form-control'}))
    email = forms.EmailField(
                            widget=forms.TextInput(attrs={'Class': 'form-control'}))
    password1 = forms.CharField(
                            label='Password',
                            max_length=100,
                            min_length=5, 
                            widget=forms.PasswordInput(attrs={'Class': 'form-control'}))
    password2 = forms.CharField(
                            label='Confirm Password',
                            max_length=100,
                            min_length=5,
                            widget=forms.PasswordInput(attrs={'Class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('Emails is already registered.')
        return email

    # def clean_password(self):
    #     """
    #     This will raise a key error because it refernces password2 field
    #     which is ran AFTER password1 validation
    #     """
    #     p1 = self.cleaned_data['password1']
    #     p2 = self.cleaned_data['password2']
    #     if p1 != p2:
    #         raise ValidationError('Password1 does not match Passaword2')
    #     return p1

    # def clean_password2(self):
    #     p1 = self.cleaned_data['password1']
    #     p2 = self.cleaned_data['password2']
    #     if p1 != p2:
    #         raise ValidationError('Password2 does not match Passaword1')
    #     return p2

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')

        # if any of those exist, if is not none
        if p1 and p2:
            if p1 != p2:
                raise ValidationError('PasswordS does not match')