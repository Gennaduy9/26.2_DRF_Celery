from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from courses.models import Course
from lessons.models import Lesson
from lessons.validators import UrlLinkCheckValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["name", "description", "preview_image", "video", "course", "owner"]
        validators = [UrlLinkCheckValidator(field='video')]


class LessonListSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = ["name", "description", "preview_image", "video", "course", "owner"]
