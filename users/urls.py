from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserProfileView, PaymentsListView, registration_user, UserListAPIView, UserRetrieveAPIView, \
    UserDeleteAPIView, UserUpdateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('payments/', PaymentsListView.as_view(), name='payments-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', registration_user, name='registration'),
    path('user/list/', UserListAPIView.as_view(), name='user-list'),
    path('user/details/<int:pk>', UserRetrieveAPIView.as_view(), name='user-details'),
    path('user/delete/<int:pk>', UserDeleteAPIView.as_view(), name='user-delete'),
    path('user/update/<int:pk>', UserUpdateAPIView.as_view(), name='user-update'),
]
