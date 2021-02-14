# Generated by Django 3.1.6 on 2021-02-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility_bills', '0003_auto_20210214_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='antenna_pay',
            field=models.FloatField(blank=True, null=True, verbose_name='Антенна'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='doorphone_pay',
            field=models.FloatField(blank=True, null=True, verbose_name='Домофон'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='doorphone_pay2',
            field=models.FloatField(blank=True, null=True, verbose_name='Домофон (Почтовая)'),
        ),
    ]