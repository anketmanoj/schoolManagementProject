from django.urls import path, include
from rest_framework import routers
from .views import USerViewSet

router = routers.DefaultRouter()
router.register(r'', USerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
