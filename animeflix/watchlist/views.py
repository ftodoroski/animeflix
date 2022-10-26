from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Watchlist, Profile, Program

from prof.serializers import ProfileWatchlistSerializer


class ProfileWatchlistView(ListAPIView, CreateAPIView, DestroyAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = ProfileWatchlistSerializer

    def get(self, request, *args, **kwargs):
        query_param = request.query_params.get('profile_id', None)

        if query_param is not None:
            queryset = Watchlist.objects.filter(profile_id=query_param)
            serializer = self.get_serializer(queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        data = {'msg': 'No profile_id parameter added'}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        profile_id = request.data.get('profile_id')
        program_id = request.data.get('program_id')
        for watchlist in Watchlist.objects.filter(profile_id=profile_id):
            if watchlist.program.id == int(program_id):
                return Response(data={'error': 'Already in watchlist'}, status=status.HTTP_400_BAD_REQUEST)

        profile = Profile.objects.get(id=profile_id)
        program = Program.objects.get(id=program_id)
        watchlist = Watchlist.objects.create(profile=profile, program=program)
        serializer = self.get_serializer(watchlist)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
