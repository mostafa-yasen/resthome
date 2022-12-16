
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProductCreateAPIView.as_view()),
    path('all', views.get_all_products),
    path('<int:pk>/', views.ProductDetailAPIView.as_view())
]
