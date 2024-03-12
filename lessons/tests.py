from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken, Token

from lessons.models import Lesson
from users.models import User, UserRoles


class LessonTestCase(APITestCase):
    """
    Класс для тестирования API уроков.

    Методы:
    - setUp: Подготовка тестового окружения.
    - test_create_lesson: Тест создания урока.
    - test_list_lesson: Тест вывода списка уроков.
    - test_destroy_lesson: Тест удаления урока.
    - test_update_lesson: Тест изменения урока.
    """

    def setUp(self) -> None:
        """
        Подготовка тестового окружения:
        - Получение JWT-токена для аутентификации клиента.
        """

        self.client = APIClient()

        self.user = User.objects.create(email="test@gmail.com", is_superuser=True, is_staff=True)
        self.client.force_authenticate(user=self.user)

        Lesson.objects.create(name='test')

    def test_create_lesson(self):
        """ Тест создания урока: отправляем данные и проверяем статус ответа. """
        data = {
            "name": "test",
            "description": "test"
        }

        response = self.client.post('/lessons/create/', data=data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_lesson(self):
        """ Тест вывода списка уроков: отправляем GET-запрос и проверяем статус ответа. """
        response = self.client.get('/lessons/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_destroy_lesson(self):
        """ Тест удаления урока: создаем урок, отправляем DELETE-запрос и проверяем статус ответа."""

        Lesson.objects.create(
            name="del_test",
            description="del_test"
        )

        response = self.client.delete('/lessons/destroy/4/')

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    # def test_update_lesson(self):
    #     """ Тест изменения урока: создаем урок, отправляем PATCH-запрос с новым описанием и проверяем статус ответа. """
    #
    #     Lesson.objects.create(
    #         name="test"
    #     )
    #     response = self.client.patch(
    #         '/lessons/update/3/'
    #     )
    #
    #     print(response.json())
    #
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )

    def test_update_lesson(self):
        """ Тест изменения урока: создаем урок, отправляем PATCH-запрос с новым описанием и проверяем статус ответа. """

        lesson = Lesson.objects.create(name="test")
        new_description = "New description"

        response = self.client.patch(
            f'/lessons/update/{lesson.id}/',
            data={"description": new_description}

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Проверка, что описание урока изменилось
        lesson.refresh_from_db()
        self.assertEqual(lesson.description, new_description)
