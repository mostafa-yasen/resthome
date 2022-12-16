from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
  discount_value = serializers.SerializerMethodField(read_only=True)

  class Meta:
    model = Product
    fields = [
      "id",
      "title",
      "content",
      "price",
      "sale_price",
      "discount_value"
    ]

  def get_discount_value(self, obj):
    if not hasattr(obj, 'id') or not isinstance(obj, Product):
      return None

    return "%.2f" %(float(obj.price) - float(obj.sale_price))
