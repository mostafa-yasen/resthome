from django.urls import path

from . import views

urlpatterns = [
  path('', views.api_home),
  path('random', views.random_product),
  path('products', views.get_all_products)
]