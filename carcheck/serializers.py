from rest_framework import serializers
from carcheck.models import Car

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    model = serializers.CharField(max_length=150)
    year = serializers.DateField()
    engine = serializers.FloatField()
    color = serializers.CharField(max_length=150)
    number = serializers.CharField(max_length=10)

