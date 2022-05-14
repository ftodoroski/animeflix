from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView, 
)
from rest_framework.settings import api_settings
from rest_framework.authentication import (
    SessionAuthentication, 
    TokenAuthentication,
)

from user.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = []


class LoginUserView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email, 
        })


class LogoutUserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        request.user.auth_token.delete()
        return Response(
            {'msg': 'Logged out'}, 
            status=status.HTTP_200_OK
        )

   
class DeleteUserView(DestroyAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class UpdateUserView(UpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
