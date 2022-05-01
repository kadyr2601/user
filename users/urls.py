from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, SubscribesViewSet

router = DefaultRouter()
router.register('', UserViewSet)
router.register('subscribes', SubscribesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
