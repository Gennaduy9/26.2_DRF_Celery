from django.http import Http404
from rest_framework import viewsets, generics, serializers
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from courses.models import Course, CourseSubscription, CoursePayment
from courses.paginators import CoursePaginator
from courses.serilzers import CourseSerializer, CoursePaymentSerializer
from courses.services import get_session
from lessons.permissions import IsSuperuser, IsOwnerOrStaff, IsModerator
from users.serilzers import UserSerializer
from courses.tasks import send_mail_about_updates


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePaginator

    def get_permissions(self):
        # Возвращает соответствующие разрешения в зависимости от действия.
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated | IsModerator]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsSuperuser]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsSuperuser]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsSuperuser | IsOwnerOrStaff | IsModerator]
        else:
            self.action = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        subscribed_users = instance.get_subscribed_users()
        # Отправляем уведомление каждому пользователю
        for user in subscribed_users:
            if user.email:
                send_mail_about_updates.delay(user.email, instance.name)

        return super().update(request, *args, **kwargs)


class SubscriptionAPIView(APIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = self.request.user
        user_data = UserSerializer(user).data

        course_id = request.data.get('course_id')

        if course_id is None:
            return Response({"message": "Отсутствует идентификатор курса в запросе"}, status=400)

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            raise Http404("Курс с таким идентификатором не найден")

        subs_item = CourseSubscription.objects.filter(user=user, course=course)

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка на курс удалена'
        else:
            CourseSubscription.objects.create(user=user, course=course)
            message = 'Подписка на курс добавлена'

        return Response({"message": message, "user": user_data})


class CoursePaymentApiView(generics.CreateAPIView):
    queryset = CoursePayment.objects.all()
    serializer_class = CoursePaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        paid_of_course = serializer.save()
        payment_link = get_session(paid_of_course)
        paid_of_course.payment_link = payment_link
        paid_of_course.save()


# class NewsletterUpdateCourseAPIView(APIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request):
#         course = get_object_or_404(Course, pk=request.data.get("course"))
#         user = self.request.user
#
#         if not Course.objects.filter(subscriptions=user).exists():
#             course.subscriptions.add(user)
#             message = f'{user.email} {course.name} обновлен!'
#             send_mail_about_updates.delay(message, course.owner.email)
#         else:
#             course.subscriptions.remove(user)
#             message = f'{user.email} удалил {course.name}!'
#         return Response({'message': message})

    # def patch(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     subscribed_users = instance.get_subscribed_users()
    #     print(subscribed_users)
    #
    #     # Проверка на последнее обновление курса
    #     if (timezone.now() - instance.last_updated).total_seconds() > 4 * 3600:
    #         # Отправляем уведомление каждому пользователю
    #         for user in subscribed_users:
    #             if user.email:
    #                 try:
    #                     send_mail_about_updates.delay(recipient_email=user.email, course_name=instance.name)
    #                 except Exception as emails:
    #                     logger.error(f"Не удалось отправить электронное письмо на адрес {user.email}: {emails}")
    #
    #     return super().update(request, *args, **kwargs)
