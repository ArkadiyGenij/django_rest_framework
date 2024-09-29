from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsModerators(BasePermission):
    """
    Проверка на роль пользователя
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Moderators').exists()


class IsOwner(BasePermission):
    """
    Проверка на владельца курса или урока
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class ModeratorPermission(BasePermission):
    """
    Определяем права модератора
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name='Moderators').exists():
            if view.action in ['list', 'retrieve', 'update', 'partial_update']:
                return True
            return False


class IsOwnerOrReadOnly(BasePermission):
    """
    Разрешение на редактирование только для владельца профиля.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user
