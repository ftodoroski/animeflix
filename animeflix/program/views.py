from django.shortcuts import render

from rest_framework import generics

from core.models import Program
from .serializers import ProgramSerializer

# class ProgramAPIView(generics.ListAPIView):
#     queryset = Program.objects.all()
#     serializer_class = ProgramSerializer





# Create your views here.
# https://www.geeksforgeeks.org/class-based-views-django-rest-framework/
# https://www.cdrf.co/
# Adding React to Django  https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react
# Make the Programs and we will figure out the rest tommorow
