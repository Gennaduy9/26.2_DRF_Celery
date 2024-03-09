from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    message = "Вы не являетесь модератором!"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsOwnerOrStaff(BasePermission):
    message = 'Вы не являетесь владельцем!'

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        for user in view.get_object().user.all():
            if request.user == user:
                return True
        return False


class IsSuperuser(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False

# class IsOwnerOrStaff(BasePermission):
#
#     def has_permission(self, request, view):
#         # Проверяем, является ли пользователь сотрудником
#         if request.user.is_staff:
#             return True
#
#         # Возвращаем True только если объект получен и пользователь является владельцем курса
#         return hasattr(view, 'get_object') and self.check_owner(request.user, view.get_object())
#
#     def check_owner(self, user, course):
#         # Проверяем, является ли пользователь владельцем курса
#         return course.user.filter(pk=user.pk).exists()


# class IsOwner(BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.user


# class IsOwner(permissions.BasePermission):
#     message = 'Вы не являетесь владельцем!'
#
#     def has_object_permission(self, request, view, obj):
#         if request.user == obj.user:
#             if view.action in ['list', 'create', 'retrieve', 'update', 'partial_update', 'destroy']:
#                 return True
#         return False
