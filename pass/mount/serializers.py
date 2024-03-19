from .models import *
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['email', 'last_name', 'first_name', 'middle_name', 'phone']


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ['winter', 'spring', 'summer', 'autumn']


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ['image', 'title']


class CoordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class PassSerializer(WritableNestedModelSerializer):
    tourist_id = UsersSerializer()
    images = ImagesSerializer(many=True)
    coordinate_id = CoordsSerializer()
    add_time = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S')
    level = LevelSerializer()

    class Meta:
        model = Pass
        fields = ['beauty_title', 'title', 'other_titles', 'connect',
                  'add_time', 'tourist_id', 'coordinate_id', 'level', 'images']

    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            data_user = data.get('user')
            validating_user_fields = [
                instance_user.last_name != data_user['last_name'],
                instance_user.first_name != data_user['first_name'],
                instance_user.middle_name != data_user['patronymic'],
                instance_user.phone != data_user['phone'],
                instance_user.email != data_user['email'],

            ]

            if data_user is not None and any(validating_user_fields):
                raise serializers.ValidationError(
                    {'Отклонено': 'Нельзя изменять данные пользователя'})
        return data
