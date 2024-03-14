from .models import *
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'last_name', 'first_name', 'middle_name', 'phone']