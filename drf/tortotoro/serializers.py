from rest_framework import serializers
from .models import Grades, Workers, Order

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = '__all__'


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



