from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('test/<int:id>/', show, name='show'),
    path('chek', chek, name='chek'),
]