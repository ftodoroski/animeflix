from rest_framework.generics import (
    RetrieveAPIView, 
    ListAPIView,
)

from core.models import Program
from .serializers import ProgramSerializer


class DetailProgramViews(RetrieveAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ListGenreProgramView(ListAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer