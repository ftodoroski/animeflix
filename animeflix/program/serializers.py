from rest_framework.serializers import ModelSerializer

from core.models import Program

class ProgramSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'