from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from account_module.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'address', 'about_user']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'id': 'message'
            })
        }

        labels = {
            'first_name': 'name',
            'last_name': 'name family',
            'avatar': 'Image profile',
            'address': 'Address',
            'about_user': 'inWither person',
        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='Password current',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='repetition Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('Password and repetition Password Contradiction have')
