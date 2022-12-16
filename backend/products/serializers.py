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
      "sale_price",
      "discount_value"
    ]

  def get_discount_value(self, obj):
    return "%.2f" %(float(obj.price) - float(obj.sale_price))
