from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from lessons.models import Lesson
from lessons.paginators import LessonPaginator
from lessons.permissions import IsOwnerOrStaff, IsModerator
from lessons.serilzers import LessonSerializer, LessonListSerializer


class LessonListView(generics.ListAPIView):
    # Представление для получения списка уроков.
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer
    pagination_class = LessonPaginator
    permission_classes = [AllowAny]


class LessonCreateView(generics.CreateAPIView):
    # Представление для создания нового урока.
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class LessonUpdateView(generics.UpdateAPIView):
    # Представление для обновления существующего урока.
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class LessonRetrieveView(generics.RetrieveAPIView):
    # Представление для получения информации об уроке
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff, IsModerator]


class LessonDestroyView(generics.DestroyAPIView):
    # Представление для удаления урока.
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]
