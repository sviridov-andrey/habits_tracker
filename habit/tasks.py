from celery import shared_task
from config import settings
from habit.models import Habit
import requests


@shared_task
def send_message_to_bot(habit_id):
    """ отправляет сообщение в телеграм-бот"""

    habit = Habit.objects.get(id=habit_id)
    requests.get(
        url=f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/sendMessage',
        params={
            'chat_id': habit.user.telegram_id,
            'text': f'Привет {habit.user}! Время выполнять {habit.action}. Место выполнения: {habit.place}.'
                    f'Это займет {habit.duration} минут!'
        }
    )
