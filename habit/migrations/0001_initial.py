# Generated by Django 4.1 on 2024-01-21 11:28

import datetime
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
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название привычки')),
                ('place', models.CharField(blank=True, max_length=100, null=True, verbose_name='место выполнения привычки')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='время выполнения привычки')),
                ('action', models.CharField(max_length=100, verbose_name='действие привычки')),
                ('is_good', models.BooleanField(default=True, verbose_name='признак приятной привычки')),
                ('period', models.CharField(choices=[('1', 'ежедневно'), ('2', 'раз в два дня'), ('3', 'раз в три дня'), ('4', 'раз в четыре дня'), ('5', 'раз в пять дней'), ('6', 'раз в шесть дней'), ('7', 'раз в семь дней')], default='daily', max_length=20, verbose_name='периодичность привычки')),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=120), verbose_name='продолжительность выполнения привычки')),
                ('is_public', models.BooleanField(default=True, verbose_name='признак публичной привычки')),
                ('prize', models.CharField(blank=True, max_length=100, null=True, verbose_name='награда')),
                ('connected_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habit.habit', verbose_name='связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='владелец')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
                'ordering': ('name',),
            },
        ),
    ]
