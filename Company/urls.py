from django.urls import path
from .views import addMedicine, afterAddMedicine, medicineList, viewOrder

urlpatterns = [
    path('addMedicine/', afterAddMedicine, name="addmedicine"),
    path('medicineList/',medicineList,name='medicineList'),
    path('viewOrder/',viewOrder,name='viewOrder')
]