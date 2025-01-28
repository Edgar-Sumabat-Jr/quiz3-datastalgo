from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_products),
    path('product/<uuid:uuid>/', views.get_product),
]
