from django.urls import path
from rest_framework.routers import DefaultRouter

from courses.apps import CoursesConfig
from courses.views import CourseViewSet, SubscriptionAPIView, CoursePaymentApiView

app_name = CoursesConfig.name

router = DefaultRouter()

router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('subscription/', SubscriptionAPIView.as_view(), name='subscription'),
    path('payment_course/create/', CoursePaymentApiView.as_view(), name='course-payment'),
] + router.urls
