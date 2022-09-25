# django
from django.shortcuts import render

# rest-framework
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# django-spectacular
from drf_spectacular.utils import extend_schema

# local-files
from ..models import User
from ..serializers.user import UserSerializer, UserCreateUpdateSerializer


class UserBaseAPIView:
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]


class UserListAPIView(UserBaseAPIView, generics.ListAPIView):
    serializer_class = UserSerializer


class UserCreateAPIView(UserBaseAPIView, generics.CreateAPIView):
    serializer_class = UserCreateUpdateSerializer


# class UserCreateAPIView(APIView):

#     @extend_schema(
#         request=UserCreateUpdateSerializer,
#         responses={200: UserSerializer},
#     )
#     def post(self, request, *args, **kwargs):
#         serializer = UserCreateUpdateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetailAPIView(UserBaseAPIView, generics.RetrieveAPIView):
    serializer_class = UserSerializer


class UserUpdateAPIView(UserBaseAPIView, generics.CreateAPIView):
    serializer_class = UserCreateUpdateSerializer


# class UserUpdateAPIView(APIView):

#     @extend_schema(
#         request=UserCreateUpdateSerializer,
#         responses={200: UserSerializer},
#     )
#     def put(self, request, pk, *args, **kwargs):
#         instance = get_object_or_404(User, pk=pk)
        
#         serializer = UserCreateUpdateSerializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)


class UserDeleteAPIView(UserBaseAPIView, generics.DestroyAPIView):
    serializer_class = UserSerializer
