# Generated by Django 3.1.6 on 2021-02-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility_bills', '0002_auto_20210214_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='antenna_pay',
            field=models.FloatField(blank=True, verbose_name='Антенна'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='doorphone_pay',
            field=models.FloatField(blank=True, verbose_name='Домофон'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='doorphone_pay2',
            field=models.FloatField(blank=True, verbose_name='Домофон (Почтовая)'),
        ),
    ]
