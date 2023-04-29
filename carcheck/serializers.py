from rest_framework import serializers
from carcheck.models import Car, CarImage, CarOwner


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    model = serializers.CharField(max_length=150)
    year = serializers.DateField()
    engine = serializers.FloatField()
    color = serializers.CharField(max_length=150)
    number = serializers.CharField(max_length=10)
    # image = serializers.ImageField()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['car_images'] = CarImageSerializer(instance.car_images.all(), many=True, context=self.context).data
        representation['image_count'] = instance.car_images.all().count()
        # representation['owner'] = instance.owner.owner.username
        representation['owner'] = 1
        return representation

    def create(self, validated_data):
        car = Car.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def get_images(self, obj):
        car_image = CarImage.objects.filter(
            car=obj.id
        )
        serializer = CarImageSerializer(car_image, many=True)
        return serializer.data

class CarImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarImage
        fields = "__all__"

class CarOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarOwner
        fields = "__all__"