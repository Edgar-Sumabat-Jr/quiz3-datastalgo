from django.contrib import admin
from .models import Product

# Register the Product model to make it appear in the Admin interface
admin.site.register(Product)
