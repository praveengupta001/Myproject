from rest_framework import serializers
from .models import Category, PestTool, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PestToolSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = PestTool
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    tool_name = serializers.ReadOnlyField(source='tool.name')

    class Meta:
        model = Order
        fields = '__all__'
