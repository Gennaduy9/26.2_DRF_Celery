from django.db import models

from courses.models import Course

NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    preview_image = models.ImageField(upload_to='lesson_previews/', **NULLABLE, verbose_name='Изображение')
    video = models.TextField(**NULLABLE, verbose_name='Ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name='Курс',
                               **NULLABLE)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='lessons', default=None,
                              verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
