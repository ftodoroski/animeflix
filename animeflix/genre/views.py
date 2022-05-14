from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from core.models import Genre, Profile
from .serializers import GenreSerializer

class ListGenreIDsView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
        



