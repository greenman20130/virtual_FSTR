from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import *
from .models import *


class UsersViewset(viewsets.ModelViewSet):
   queryset = Users.objects.all()
   serializer_class = UsersSerializer


class CoordsViewset(viewsets.ModelViewSet):
   queryset = Coords.objects.all()
   serializer_class = CoordsSerializer


class LevelViewset(viewsets.ModelViewSet):
   queryset = Level.objects.all()
   serializer_class = LevelSerializer