from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from courses.models import Course
from users.models import User


class SubscribeTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email="test@gmail.com", is_superuser=True, is_staff=True)
        self.client.force_authenticate(user=self.user)
        Course.objects.create(name='test')

    def test_retrieve_subscribe(self):
        """ Тестирование функционала работы подписки на обновления курса"""

        data = {
            "course_id": 1,
            "user": 1
        }

        response = self.client.post(
            '/courses/subscription/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
