from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    preview_image = models.ImageField(upload_to='course_previews/', verbose_name='Изображение', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Владелец',
                                   **NULLABLE)
    price = models.PositiveIntegerField(null=True, verbose_name='Цена')

    def __str__(self):
        return self.name

    def get_subscribed_users(self):
        return [subscription.user for subscription in self.subscriptions.all() if subscription.user is not None]

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class CourseSubscription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subscriptions', verbose_name='Курс')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь', null=True)

    def __str__(self):
        return f"{self.user} {self.course}"

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class CoursePayment(models.Model):
    name = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Название продукта', **NULLABLE)
    price_amount = models.CharField(verbose_name='Цена платежа', **NULLABLE)
    payment_link = models.URLField(max_length=400, verbose_name='Ссылка на оплату', **NULLABLE)
    payment_id = models.CharField(max_length=255, verbose_name='Идентификатор платежа', **NULLABLE)

    def __str__(self):
        return self.payment_id

    class Meta:
        verbose_name = 'Оплата курса'
        verbose_name_plural = 'Оплата курсов'
