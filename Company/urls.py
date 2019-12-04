from django.urls import path
from .views import addMedicine, getPharmacistOnId, getMedicineOnId, getMedicineTypeOnId, getAddMedicinePage, medicineList,getSoldMedicinesPage,getSoldMedicineWithoutPrescription

urlpatterns = [
    path('addMedicine/', getAddMedicinePage, name="addmedicine"),
    path('medicineList/',medicineList,name='medicineList'),
    path('soldMedicines/',getSoldMedicinesPage,name='soldMedicines'),
    path('soldMedicines/getSoldMedicineWithoutPrescription',getSoldMedicineWithoutPrescription,name='getSoldMedicineWithoutPrescription'),
    path('soldMedicines/getMedicineOnId/',getMedicineOnId,name='getMedicineOnId'),
    path('soldMedicines/getMedicineTypeOnId/',getMedicineTypeOnId,name='getMedicineTypeOnId'),
    path('soldMedicines/getPharmacistOnId/',getPharmacistOnId,name='getPharmacistOnId')
    
]