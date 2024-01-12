from datetime import timedelta
from django.db import models
from config import settings
from users.utils import NULLABLE


class Habit(models.Model):
    """ Модель привычки """

    PERIODICTY_CHOICES = (
        ('daily', 'ежедневно'),
        ('weekly', 'еженедельно'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец')
    name = models.CharField(max_length=100, verbose_name='название привычки')
    place = models.CharField(max_length=100, **NULLABLE, verbose_name='место выполнения привычки')
    time = models.TimeField(**NULLABLE, verbose_name='время выполнения привычки')
    action = models.CharField(max_length=100, verbose_name='действие привычки')
    is_good = models.BooleanField(default=True, verbose_name='признак приятной привычки')
    connected_habit = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='связанная привычка')
    period = models.CharField(max_length=20, choices=PERIODICTY_CHOICES, default='daily',
                              verbose_name='периодичность привычки')
    duration = models.DurationField(default=timedelta(minutes=2),
                                    verbose_name='продолжительность выполнения привычки')
    is_public = models.BooleanField(default=True, verbose_name='признак публичной привычки')
    prize = models.CharField(max_length=100, verbose_name='награда', **NULLABLE)

    def __str__(self):
        return f'Пользователь: {self.user} - привычка: {self.name}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('name',)
