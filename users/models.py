from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from courses.models import Course
from lessons.models import Lesson

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, **NULLABLE, unique=True, verbose_name='Телефон')
    avatar = models.ImageField(**NULLABLE, upload_to='users', verbose_name='Аватар')
    country = models.CharField(**NULLABLE, max_length=100, verbose_name='Страна')
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payment(models.Model):
    METHOD_CHOICES = [('transfer', 'Перевод на счет'), ('cash', 'Наличные'), ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    pay_date = models.DateField(verbose_name='Дата оплаты')
    pay_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    pay_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    money = models.IntegerField(verbose_name='Оплаченная сумма')
    pay_method = models.CharField(choices=METHOD_CHOICES, default=METHOD_CHOICES[0],
                                  verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.money}'

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплата'
