from rest_framework import viewsets
from users.serializers import UserSerializer, User, Subscribes, SubscribesSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class SubscribesViewSet(viewsets.ModelViewSet):
    serializer_class = SubscribesSerializer
    queryset = Subscribes.objects.all()
