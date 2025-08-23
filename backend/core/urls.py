from django.urls import path
from .views import create_address

urlpatterns = [
    path("generate/", create_address, name="generate_address"),
]
