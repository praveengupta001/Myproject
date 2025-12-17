from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, PestTool, Order
from .serializers import CategorySerializer, PestToolSerializer, OrderSerializer

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PestToolViewSet(viewsets.ModelViewSet):
    queryset = PestTool.objects.all()
    serializer_class = PestToolSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
