from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PestToolViewSet, OrderViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('tools', PestToolViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
