from django.urls import path
from .views import addMedicine, afterAddMedicine

urlpatterns = [
    path('addMedicine/', afterAddMedicine, name="addmedicine"),
]