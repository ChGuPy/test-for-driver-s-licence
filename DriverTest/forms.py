# -*- coding:utf-8 -*-
from django import forms
from  models import Question
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class UserLoginForm(forms.Form):
    login = forms.CharField(label=u'Логин пользователя', max_length=30)
    password = forms.CharField(label=u'Пароль пользователя', widget=forms.PasswordInput(), max_length=30)

    def clean_login(self):
        login = self.cleaned_data['login']
        try:
            user = User.objects.get(username=login)
            return user
        except ObjectDoesNotExist:
            raise forms.ValidationError(u'Такой пользователь не зарегестрирован')

    def clean_password(self):
        password = self.cleaned_data['password']
        return password



class TestsForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['is_active']
