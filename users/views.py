from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from lessons.permissions import IsSuperuser, IsModerator, IsOwnerOrStaff
from users.models import Payment, User
from users.serilzers import PaymentSerializer, UserSerializer


class PaymentViewSet(ModelViewSet):
    # Класс представления для модели платежа (Payment).
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_fields = ('pay_course', 'pay_lesson', 'pay_method',)
    ordring_fields = ('pay_date',)


class UserViewSet(ModelViewSet):
    # Класс представления для модели пользователя (User).
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # Возвращает соответствующие разрешения в зависимости от действия.
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        elif self.action == 'list':
            self.permission_classes = [IsSuperuser | IsModerator]
        elif self.action == 'destroy':
            self.permission_classes = [IsSuperuser | IsOwnerOrStaff]
        elif self.action == 'update':
            self.permission_classes = [IsSuperuser | IsOwnerOrStaff]
        elif self.action == 'retrieve':
            self.permission_classes = [IsSuperuser | IsOwnerOrStaff | IsModerator]
        else:
            self.action = [IsOwnerOrStaff]
        return [permission() for permission in self.permission_classes]

