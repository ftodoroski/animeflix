from random import choice

from rest_framework.serializers import (
    ModelSerializer, 
    Serializer,
    SerializerMethodField,
    PrimaryKeyRelatedField,
    IntegerField
)

from core.models import (
    Profile, 
    Program,
    Watchlist,
)


class ShowcaseID:
    def get_showcase_id(self, obj):
        program_ids = [program.id for program in Program.objects.all()]
        return choice(program_ids) 


class ListProfileSerializer(ModelSerializer, ShowcaseID):
    showcase_id = SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class DetailProfileWatchlistSerializer(ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ['id', 'program_id', 'created_at']


class DetailProfileSerializer(ModelSerializer, ShowcaseID,):
    showcase_id = SerializerMethodField(read_only=True)
    watchlist = SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'name',
            'user_id',
            'profile_num', 
            'showcase_id',
            'watchlist'
        ]

    def get_watchlist(self, obj):
        qs = Watchlist.objects.filter(profile_id=obj.id)
        serializer = DetailProfileWatchlistSerializer(qs, many=True)
        return serializer.data
