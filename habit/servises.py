from django_celery_beat.models import CrontabSchedule, PeriodicTask
from config import settings


def create_reminder(habit):
    """ Создает напоминание о привычке """

    crontab_schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=habit.time.minute,
        hour=habit.time.hour,
        day_of_month=f'*/{habit.period}',
        day_of_week='*',
        month_of_year='*',
        timezone=settings.TIME_ZONE
    )

    PeriodicTask.objects.create(
        crontab=crontab_schedule,
        name=f'Habit Task - {habit.name}',
        task='habit.tasks.send_message_to_bot',
        args=[habit.id],
    )


def delete_reminder(habit):
    """ Удаляет напоминание о привычке """

    task_name = f'send_message_to_bot_{habit.id}'
    PeriodicTask.objects.filter(name=task_name).delete()


def update_reminder(habit):
    """ Обновляет напоминание о привычке """

    delete_reminder(habit)
    create_reminder(habit)
