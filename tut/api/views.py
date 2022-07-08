from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Where we are going to write all of our endpoints of the website
# Create your views here.

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
