# Generated by Django 3.1.6 on 2021-02-14 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('month_pay', models.CharField(max_length=50, verbose_name='За месяц')),
                ('communal_pay', models.FloatField(verbose_name='Коммунальный платеж')),
                ('electric_pay', models.FloatField(verbose_name='Электричество')),
                ('internet_pay', models.FloatField(verbose_name='Интернет')),
                ('antenna_pay', models.FloatField(blank=True, default=None, verbose_name='Антенна')),
                ('doorphone_pay', models.FloatField(blank=True, default=None, verbose_name='Домофон')),
                ('doorphone_pay2', models.FloatField(blank=True, default=None, verbose_name='Домофон (Почтовая)')),
                ('current_user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='current_user_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
    ]
