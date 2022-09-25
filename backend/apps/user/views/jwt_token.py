from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

# local-files
from ..serializers.jwt_token import (
    CustomTokenObtainPairSerializer,
    CustomTokenRefreshSerializer,
)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer
