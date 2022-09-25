# django
from django.urls import path

# local-files
from ..views.jwt_token import CustomTokenObtainPairView, CustomTokenRefreshView


app_name = 'auth'


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]