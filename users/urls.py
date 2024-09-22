from django.urls import path

from users.apps import UsersConfig
from users.views import UserProfileView, PaymentsListView

app_name = UsersConfig.name

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('payments/', PaymentsListView.as_view(), name='payments-list'),
]
