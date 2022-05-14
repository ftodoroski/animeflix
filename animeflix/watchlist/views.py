from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Watchlist

from prof.serializers import DetailProfileWatchlistSerializer


class ListProfileWatchlistView(ListAPIView):
    queryset = Watchlist.objects.all()

    def get(self, request, *args, **kwargs):
        query_param = request.query_params.get('profileID', None)

        if query_param is not None:
            queryset = Watchlist.objects.filter(profile_id=query_param)
            serializer = DetailProfileWatchlistSerializer(queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        data = {'msg': 'No profileID parameter added'}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)