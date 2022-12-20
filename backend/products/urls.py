
from django.urls import path
from .views import product_mixin_api_view

urlpatterns = [
    path('', product_mixin_api_view),
    path('<int:pk>/', product_mixin_api_view),
    path('<int:pk>/update/', product_mixin_api_view),
    path('<int:pk>/delete/', product_mixin_api_view),
]
