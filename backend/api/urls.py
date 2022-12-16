from django.urls import path, include

from . import views

urlpatterns = [
  path('', views.api_home),
  path('random/', views.random_product),
  path('product/new', views.create_product),
  path('products/', include('products.urls')),
]
