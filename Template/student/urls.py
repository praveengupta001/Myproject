from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_students, name='get_students'),
    path('add/', views.add_student, name='add_student'),
    path('<int:id>/', views.get_student, name='get_student'),
]
