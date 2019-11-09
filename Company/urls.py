from django.urls import path
from .views import addMedicine, afterAddMedicine, medicineList

urlpatterns = [
    path('addMedicine/', afterAddMedicine, name="addmedicine"),
    path('medicineList',medicineList,name='medicineList')
]