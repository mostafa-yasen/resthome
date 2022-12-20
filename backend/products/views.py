from products.models import Product
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework import authentication, generics, mixins, permissions

from products.serializers import ProductSerializer


class ProductAPIMixin(
  mixins.CreateModelMixin,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  mixins.RetrieveModelMixin,
  mixins.ListModelMixin,
  generics.GenericAPIView
):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  authentication_classes = [authentication.SessionAuthentication]
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def get(self, request, *args, **kwargs):
    if kwargs.get('pk'):
      return self.retrieve(request, *args, **kwargs)

    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return super().destroy(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return super().update(request, *args, **kwargs)

  def perform_create(self, serializer):
    content = serializer.validated_data.get("content")
    content = content or serializer.validated_data.get("title")
    serializer.save(content=content)

    # return super().perform_create(serializer)

product_mixin_api_view = ProductAPIMixin.as_view()

# class ProductDetailAPIView(generics.RetrieveAPIView):
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer


# class ProductListCreateAPIView(generics.ListCreateAPIView):
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer

#   def perform_create(self, serializer):
#     instance = serializer.save()
#     if not instance.content:
#       instance.content = instance.title
#       instance.save()


# class ProductUpdateAPIView(generics.UpdateAPIView):
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer
#   lookup_field = 'pk'


# class ProductDeleteAPIView(generics.DestroyAPIView):
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer
#   lookup_field = 'pk'

#   def perform_destroy(self, instance: Product):
#     super().perform_destroy(instance)
