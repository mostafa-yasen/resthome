from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from products.serializers import ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def perform_create(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = instance.title
      instance.save()


class ProductUpdateAPIView(generics.UpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
