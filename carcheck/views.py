from django.http import Http404
from rest_framework.views import APIView
from rest_framework import response, status
from carcheck.models import Car
from carcheck.serializers import CarSerializer


class CarListAPIView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,
                                     status=status.HTTP_201_CREATED
                                     )
        return response.Response(status=status.HTTP_400_BAD_REQUEST)
