from django import forms
from django.contrib.auth.models import User

from utility_bills.models import Payments


class PaymentsForm(forms.ModelForm):
    MONTHS = [
        ('Январь', 'Январь'), ('Февраль', 'Февраль'), ('Март', 'Март'), ('Апрель', 'Апрель'),
        ('Май', 'Май'), ('Июнь', 'Июнь'), ('Июль', 'Июль'), ('Август', 'Август'), ('Сентябрь', 'Сентябрь'),
        ('Октябрь', 'Октябрь'), ('Ноябрь', 'Ноябрь'), ('Декабрь', 'Декабрь')
    ]

    # current_user = forms.ModelChoiceField(label='Имя пользователя', queryset=User.objects.all(), widget=forms.Select(
    #     attrs={'class': 'form-control ', 'aria-label': "Disabled select example",  'disabled': ''}))

    month_pay = forms.ChoiceField(label='За Месяц', choices=MONTHS, widget=forms.Select(attrs={
        'class': 'form-control', 'placeholder': 'Месяц'}))

    communal_pay = forms.DecimalField(label='Коммунальный платеж', max_digits=6, min_value=0,
                                      widget=forms.NumberInput(attrs={
                                          'class': 'form-control', 'placeholder': 'Введите сумму за месяц'}))
    electric_pay = forms.DecimalField(label='Электричество', max_digits=6, min_value=0,
                                      widget=forms.NumberInput(attrs={
                                          'class': 'form-control', 'placeholder': 'Введите сумму за месяц'}))
    internet_pay = forms.DecimalField(label='Интернет', max_digits=6, min_value=0, widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите сумму за месяц'}))

    antenna_pay = forms.DecimalField(label='Антенна', max_digits=6, min_value=0, required=False,
                                     widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите сумму за месяц'}))

    doorphone_pay = forms.DecimalField(label='Домофон', max_digits=6, min_value=0, required=False,
                                       widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите сумму за месяц'}))

    doorphone_pay2 = forms.DecimalField(label='Домофон (Почтовая)', required=False, max_digits=6, min_value=0,
                                        widget=forms.NumberInput(attrs={
                                            'class': 'form-control', 'placeholder': 'Введите сумму за месяц'}))

    class Meta:
        model = Payments

        fields = [
            'month_pay', 'communal_pay', 'electric_pay', 'internet_pay', 'antenna_pay',
            'doorphone_pay', 'doorphone_pay2'
        ]
