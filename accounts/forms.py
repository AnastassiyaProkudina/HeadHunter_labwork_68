from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


class LoginForm(forms.Form):
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
    )


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', strip=False, required=True,
                                       widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('is_employer', 'username', 'avatar', 'password', 'password_confirm', 'email', 'phone',)
        labels = {'username': 'Имя',
                  'avatar': 'Фото профиля',
                  'password': 'пароль',
                  'password_confirm': 'подтверждение пароля',
                  'email': 'Email',
                  'phone': 'Phone',
                  'is_employer': 'Работодатель'}

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        employer = self.cleaned_data.get('is_employer')
        group_employer = Group.objects.get(pk=2)
        group_seeker = Group.objects.get(pk=1)
        if commit:
            user.save()
            if employer == True:
                user.groups.add(group_employer)
            else:
                user.groups.add(group_seeker)
        return user