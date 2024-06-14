from datetime import datetime

from django.contrib.auth.forms import UserCreationForm

from .models import CreateUserModel, CreateWydarzenieModel
from django.forms import forms
from django.core.exceptions import ValidationError
from django.forms import (
    ModelForm, CharField, IntegerField, DecimalField, ChoiceField, DateField, Textarea, DateTimeField,
    SelectDateWidget, )

from django.contrib.auth.models import User


class SingUpForm(UserCreationForm):
    class Meta:
        model = CreateUserModel
        fields = ['first_name', 'last_name', 'username', 'email']

    def save(self, commit=True):
        self.instance.is_active = False
        return super().save(commit)


def title_valid(value):
    if value == " " * len(value):
        raise ValidationError('Tytu nie moze zawierac samych bialych znakow')


def data_valid(value):
    if value < datetime.now().date():
        raise ValidationError('data nie moze byc wstawiona wsteczna')


def dec_valid(value):
    if len(value) < 20:
        raise ValidationError('Opis musi zawierac conajmniej 20 znakow')


class UtworzWydarzenieForm(ModelForm):
    class Meta:
        model = CreateWydarzenieModel
        exclude = ['user_append']

    title = CharField(max_length=100, validators=[title_valid])
    deta_open = DateField(widget=SelectDateWidget, validators=[data_valid])
    deta_close = DateField(widget=SelectDateWidget, validators=[data_valid])
    description = CharField(widget=Textarea, validators=[dec_valid])





class EventSearchForm(forms.Form):
    SEARCH_CHOICES = [
        ('future', 'Przyszłe'),
        ('ongoing_future', 'Trwające i przyszłe'),
        ('all', 'Wszystkie')
    ]

    query = CharField(label='Nazwa wydarzenia', max_length=100, required=False)
    search_type = ChoiceField(label='Typ wyszukiwania', choices=SEARCH_CHOICES, required=False)






