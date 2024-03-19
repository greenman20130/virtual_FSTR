from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.response import Response


class UsersViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class CoordsViewset(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewset(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImagesViewset(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PassViewset(viewsets.ModelViewSet):
    queryset = Pass.objects.all()
    serializer_class = PassSerializer
    filterset_fields = ('tourist_id__email',)
    

    def create(selfself, request, *args, **kwargs):
        serializer = PassSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': None,
                'id': serializer.data['id'],
            })

        if status.HTTP_400_BAD_REQUEST:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Bad Request',
                'id': None,
            })

        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Ошибка подключения к базе данных',
                'id': None,
            })
        

    def partial_update(self, request, *args, **kwargs):
        pereval = self.get_object()

        if pereval.status == 'new':
            serializer = PassSerializer(
                pereval, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'state': '1',
                    'message': 'Запись успешно изменена',
                })

            else:
                return Response({
                    'state': '0',
                    'message': serializer.errors
                })

        else:
            return Response({
                'state': '0',
                'message': f'Отклонено! Причина: {pereval.get_status_display()}'
            })
