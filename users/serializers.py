from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import Subscribes
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']


class SubscribesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribes
        fields = '__all__'
