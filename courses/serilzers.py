from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from courses.models import Course, CourseSubscription, CoursePayment
from lessons.models import Lesson
from lessons.serilzers import LessonSerializer
from lessons.validators import UrlLinkCheckValidator


class CourseSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    #link_of_payment = serializers.URLField()

    # Cоздание поля для подсчёта уроков
    lesson_count = SerializerMethodField()

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.pk).count()

    def get_is_subscribed(self, obj):
        # Получаем текущего пользователя из запроса
        user = self.context['request'].user

        # Проверка подписки пользователя на этот курс
        if user.is_authenticated:
            return CourseSubscription.objects.filter(user=user, course=obj.pk).exists()
        else:
            return False

    class Meta:
        model = Course
        fields = ["name", "preview_image", "description", "lesson_count", "owner", "is_subscribed"]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = ["course", "user"]


class CoursePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePayment
        fields = '__all__'
