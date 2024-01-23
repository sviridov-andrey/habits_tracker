from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from habit.models import Habit
from users.models import User


class InitialTestCase(APITestCase):
    """Создание тестовых пользователя и привычки"""

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@example.com', password='123')
        self.client.force_authenticate(user=self.user)

        response = self.client.post('/users/token/', {"email": "test@example.com", "password": "123"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.habit = Habit.objects.create(
            user=self.user,
            name='Тестовая привычка',
            place='Тестовое место',
            time='12:00:00',
            action='Тестовое действие',
            is_good=False,
            period='1',
            duration='00:02:00',
            is_public=True,
        )


class HabitTestCase(InitialTestCase):

    def test_create_habit(self):
        """Тест создания привычки"""

        data = {
            "id": self.habit.id + 1,
            "user": self.user.id,
            "name": "Тестовая привычка_2",
            "place": "Тестовое место_2",
            "time": "13:00:00",
            "action": "Тестовое действие_2",
            "is_good": False,
            "period": '1',
            "duration": '00:01:00',
            "is_public": True,
        }

        response = self.client.post(reverse('habit:habit_create'), data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_habit(self):
        """Тест вывода списка привычек"""

        response = self.client.get(reverse('habit:habit_list'))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(Habit.objects.all().count(), 1)

    def test_retrieve_habit(self):
        """Тест детальной информации о привычке"""

        response = self.client.get((reverse('habit:habit_detail', kwargs={'pk': self.habit.id})))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": self.habit.pk,
                "user": self.user.pk,
                "name": "Тестовая привычка",
                "place": "Тестовое место",
                "time": "12:00:00",
                "action": "Тестовое действие",
                "is_good": False,
                "period": "1",
                "duration": "00:02:00",
                "is_public": True,
                "connected_habit": None,
                "prize": None,

            }
        )

    def test_update_habit(self):
        """Тест обновления привычки"""

        data = {"place": 'update'}

        response = self.client.patch(
            reverse('habit:habit_change', kwargs={'pk': self.habit.id}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['place'],
            data['place']
        )

    def test_destroy_habit(self):
        """Тест удаления привычки"""

        response = self.client.delete(
            reverse('habit:habit_delete', kwargs={'pk': self.habit.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
