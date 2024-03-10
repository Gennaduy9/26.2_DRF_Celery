from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_mail_about_updates(recipient_email, course_name):
    '''
    В этом скрипте электронное письмо отправляется, когда курс обновляется для тех пользователей,
    которые на него подписаны.
    '''
    send_mail(
        subject='course update notification',
        message=f"Курс {course_name} обновлен. Ознакомьтесь с новыми материалами!",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient_email],
        fail_silently=False
    )
