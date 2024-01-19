from habit.models import Habit
import requests


def send_message_to_bot(habit_id):
    """ функция отправки сообщения в телеграм-бот
    chat_id: id чата
    message: передаваемое сообщение
    """
    habit = Habit.objects.get(id=habit_id)
    requests.get(
        url=f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/sendMessage',
        params={
            'chat_id': habit.user.telegram_id,
            'text': f'Привет {habit.user}! Время {habit.time}. Пора идти в {habit.place} и сделать {habit.action}. ' \
                    f'Это займет {habit.duration} минут!'
        }
    )