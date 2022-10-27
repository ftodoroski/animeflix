from rest_framework.generics import (
    RetrieveAPIView, 
    ListAPIView,
)
from rest_framework.response import Response
from rest_framework import status

from core.models import Program
from .serializers import ProgramSerializer


class DetailProgramViews(RetrieveAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ListProgramView(ListAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ListFilterProgramView(ListAPIView):
    serializer_class = ProgramSerializer

    def startswith_search(self, program, query):
        if (program.title.lower().startswith(query.lower())):
            return program.title
        elif (program.director.lower().startswith(query.lower())):
            return program.director
        else:
            for genre in program.genres.all():
                if (genre.name.lower().startswith(query.lower())):
                    return genre.name

        return None
        
    def includes_search(self, program, query):
        if (not program.title.lower().startswith(query.lower()) and query.lower() in program.title.lower()):
            return [program.title]
        elif (not program.director.lower().startswith(query.lower()) and query.lower() in program.director.lower()):
            return [program.director]
        else:
            genre_names = []
            for genre in program.genres.all():
                if (not genre.name.lower().startswith(query.lower()) and query.lower() in genre.name.lower()):
                    return [genre.name]
                else:
                    genre_names.append(genre.name)
            
            return [program.title, program.director] + genre_names

    def develop_searchlist_and_recommendation(self, query):
        queryset = Program.objects.all()

        searchlist = []
        programs = []

        for program in queryset:
            search_item = self.startswith_search(program, query)
            print(program)
            if (search_item is not None) and (len(searchlist) < 10):
                programs.append(program)
                searchlist.append(search_item) if search_item not in searchlist else None

        for program in queryset:
            search_item = self.includes_search(program, query)
            if len(searchlist) < 12 and search_item not in searchlist:
                searchlist.extend(search_item)

        return [programs, list(set(searchlist))]

    def get(self, request, *args, **kwargs):
        search_query = self.request.query_params.get('search_query')
        programs, searchlist = self.develop_searchlist_and_recommendation(search_query)

        serialized_data = self.get_serializer(programs, many=True).data

        if len(programs) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = {
            'programs': serialized_data,
            'searchlist': searchlist
        }

        return Response(response)

