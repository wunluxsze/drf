from django.contrib import admin
from django.urls import path, include
from .views import worker_detail, grades_list, workers_list, grade_detail, order_detail, orders_list

urlpatterns = [
    path('workers', workers_list),
    path('orders', orders_list),
    path('grades', grades_list),
    path('worker/<int:pk>', worker_detail),
    path('order/<int:pk>', order_detail),
    path('grade/<int:pk>', grade_detail),
]