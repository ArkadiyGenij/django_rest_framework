# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import User, Payments
from users.permissions import IsOwnerOrReadOnly
from users.serializers import UserSerializer, PaymentsSerializer, UserRegistrationSerializer, UserDetailSerializer, \
    UserPublicSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    Профиль пользователя
    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.user == self.get_object():
            return UserDetailSerializer
        return UserPublicSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        if pk == 'me' or pk == str(self.request.user.pk):
            return self.request.user
        return super().get_object()


class PaymentsListView(generics.ListAPIView):
    """
    Список всех совершенных платежей с фильтрами и сортировкой
    """
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['payment_date', 'paid_lesson', 'paid_course', 'payment_method']
    ordering_fields = ['payment_date', 'paid_lesson', 'paid_course', 'payment_method']
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
def registration_user(request):
    """
    Метод регистрации пользователя
    :param request: запрос на создание пользователя и его данные
    :return: ответ от сервера
    """
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(generics.ListAPIView):
    """
    Получение всех пользователей
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Получения пользователя по id
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDeleteAPIView(generics.DestroyAPIView):
    """
    Удаление пользователя по id
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
