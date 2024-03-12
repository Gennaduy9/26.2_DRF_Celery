from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        superuser = User.objects.create(
            email='admin@mail.com',
            first_name='Admin',
            last_name='SkyPro',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        superuser.set_password('123qwe456rty')
        superuser.save()

        user1 = User.objects.create(
            email='user1@sky.com',
            is_active=True,
            is_staff=False,
            is_superuser=False
        )

        user1.set_password('user1')
        user1.save()

        user2 = User.objects.create(
            email='user2@sky.com',
            is_active=True,
            is_staff=False,
            is_superuser=False
        )

        user2.set_password('user2')
        user2.save()

        user3 = User.objects.create(
            email='myparents2@yandex.ru',
            first_name='Test1',
            last_name='Test2',
            is_active=True,
            is_staff=True,
            is_superuser=False
        )

        user3.set_password('123qwe456rty')
        user3.save()
