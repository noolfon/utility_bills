from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Payments(models.Model):
    # Добавить поля домофон, домофон  Антена, дата со временем.
    date_create = models.DateTimeField(auto_now_add=True)
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True,
                                     related_name='current_user_set')
    month_pay = models.CharField(max_length=50, verbose_name='За месяц')
    communal_pay = models.FloatField(verbose_name='Коммунальный платеж')
    electric_pay = models.FloatField(verbose_name='Электричество')
    internet_pay = models.FloatField(verbose_name='Интернет')
    antenna_pay = models.FloatField(verbose_name='Антенна', blank=True, null=True)
    doorphone_pay = models.FloatField(verbose_name='Домофон', blank=True, null=True)
    doorphone_pay2 = models.FloatField(verbose_name='Домофон (Почтовая)', blank=True, null=True)

    # def __str__(self):
    #     return f'Коммунальный платеж - {self.communal_pay},' \
    #            f'Электричество - {self.electric_pay}, Интренет - {self.internet_pay}.' \
    #            f'{self.current_user.id}'

    # после добавления записи в эту таблицу с помощью класса форм сформированной для этой таблицы и генерика createview
    # эта функция делает редирект на страницу с записью после ее добавления
    def get_absolute_url(self):
        return reverse('utility_bills:detail', kwargs={'pk': self.pk})

    class Meta:
        # Русификация
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        # Сортирвоака при отображении
        ordering = ['date_create']
