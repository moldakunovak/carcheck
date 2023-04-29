from django.http import Http404
from rest_framework.views import APIView
from rest_framework import response, status
from carcheck.models import Car, CarOwner
from carcheck.serializers import CarSerializer, CarImageSerializer, CarOwnerSerializer


class CarListAPIView(APIView):

    def get(self, request):
        print(request.user.id)
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


class DetailCarAPIView(APIView):
    def get_object(self, number):
        try:
            return Car.objects.get(number=number)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, number):
        car = self.get_object(number)
        serializer = CarSerializer(car)
        return response.Response(serializer.data,
                                 status=status.HTTP_200_OK
                                 )

    def put(self, request, number):
        car = self.get_object(number)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, number):
        car = self.get_object(number)
        car.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)





class CreateImageAPIView(APIView):

    def post(self, request):
        serializer = CarImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,
                                     status=status.HTTP_201_CREATED
                                     )
        return response.Response(status=status.HTTP_400_BAD_REQUEST)


class CreateOwnerAPIView(APIView):

    def get(self, request):
        car_owners = CarOwner.objects.all()
        serializer = CarOwnerSerializer(car_owners, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class DetailCarOwnerAPIView(APIView):
    def get_object(self, owner):
        try:
            return CarOwner.object.get(owner=owner)
        except CarOwner.DoesNotExist:
            raise Http404


    def get(self, request, owner):
        car = self.get_object(owner)
        serializer = CarOwnerSerializer(car)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, owner):
        car = self.get_object(owner)
        serializer = CarOwnerSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, owner):
        car = self.get_object(owner)
        car.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)