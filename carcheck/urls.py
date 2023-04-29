from django.urls import path
from .views import CarListAPIView, DetailCarAPIView, CreateImageAPIView, CreateOwnerAPIView

urlpatterns = [
    path('cars/', CarListAPIView.as_view()),
    path('cars/<str:number>/', DetailCarAPIView.as_view()),
    path('cars/images/', CreateImageAPIView.as_view()),
    path('cars/owners/', CreateOwnerAPIView.as_view()),
    path('cars/<int:owner>/', CreateOwnerAPIView.as_view()),
]

