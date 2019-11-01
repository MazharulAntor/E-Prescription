from django.urls import path
from .views import addMedicine, afterAddMedicine

urlpatterns = [
    path('addmed/', addMedicine, name="addmedicine"),
]