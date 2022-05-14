from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView, 
    UpdateAPIView,
    DestroyAPIView,
)

from core.models import Profile, User
from .serializers import (
    ListProfileSerializer, 
    DetailProfileSerializer,
)


class ListCreateProfileView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ListProfileSerializer
    
    def post(self, request, *args, **kwargs):
        user = User.objects.get(email=request.user)
        qs = self.get_queryset().filter(user_id=user.id)
        
        if len(qs) < 4:
            return self.create(request, *args, **kwargs)
        data = {'msg': 'Unable to add more profiles. Only 4 profiles per user'}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        user = User.objects.get(email=request.user)
        queryset = self.get_queryset().filter(user_id=user.id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class DetailProfileView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = DetailProfileSerializer


class UpdateProfileView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ListProfileSerializer


class DeleteProfileView(DestroyAPIView):
    queryset = Profile.objects.all()
