from rest_framework.serializers import (
    ModelSerializer,
    Serializer, 
    SerializerMethodField, 
    CharField,
    IntegerField,
)

from core.models import Program

class GenreSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(read_only=True)
    programs = SerializerMethodField(read_only=True)

    def get_programs(self, obj):    
        programs = Program.objects.filter(genres=obj)
        serializer = ProgramGenreSerializer(programs, many=True)
        return serializer.data


class ProgramGenreSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = ['id']