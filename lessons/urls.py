from django.urls import path
from lessons.apps import LessonsConfig
from lessons.views import LessonListView, LessonCreateView, LessonUpdateView, LessonRetrieveView, LessonDestroyView

app_name = LessonsConfig.name

urlpatterns = [
    path('', LessonListView.as_view(), name='lesson_list'),
    path('create/', LessonCreateView.as_view(), name='lesson_create'),
    path('update/<int:pk>/', LessonUpdateView.as_view(), name='lesson_update'),
    path('retrieve/<int:pk>/', LessonRetrieveView.as_view(), name='lesson_retrieve'),
    path('destroy/<int:pk>/', LessonDestroyView.as_view(), name='lesson_destroy'),
]
