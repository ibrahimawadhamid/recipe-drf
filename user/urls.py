from django.urls import path

from .views import CreateUserView, CreateTokenView
from .apps import UserConfig

app_name = UserConfig.name

urlpatterns = [
    path('create/', CreateUserView.as_view(), name="create"),
    path('token/', CreateTokenView.as_view(), name="token"),
]
