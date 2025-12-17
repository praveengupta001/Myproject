from django.contrib import admin
from .models import Category, PestTool, Order

# Register your models here.

admin.site.register(Category)
admin.site.register(PestTool)
admin.site.register(Order)
