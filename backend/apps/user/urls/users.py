# django
from django.urls import path

# local-files
from ..views.user import (
    UserListAPIView, UserDetailAPIView, UserUpdateAPIView, UserDeleteAPIView, UserCreateAPIView
)


app_name = 'users'

urlpatterns = [
    path('list/', UserListAPIView.as_view(), name='user-list'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('detail/<uuid:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('update/<uuid:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<uuid:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),
]
