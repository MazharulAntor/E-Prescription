from django.urls import path
<<<<<<< HEAD
from .views import addMedicine, getPharmacistOnId, getMedicineOnId, getMedicineTypeOnId, getAddMedicinePage, medicineList,getSoldMedicinesPage,getSoldMedicineWithoutPrescription
=======

from .views import addMedicine, getAddMedicinePage, medicineList, viewOrder
>>>>>>> e62f9df3ed8bef3fbed98cd72b1f59bd1345f1ff

urlpatterns = [
    path('addMedicine/', getAddMedicinePage, name="addmedicine"),
    path('medicineList/',medicineList,name='medicineList'),
<<<<<<< HEAD
    path('soldMedicines/',getSoldMedicinesPage,name='soldMedicines'),
    path('soldMedicines/getSoldMedicineWithoutPrescription',getSoldMedicineWithoutPrescription,name='getSoldMedicineWithoutPrescription'),
    path('soldMedicines/getMedicineOnId/',getMedicineOnId,name='getMedicineOnId'),
    path('soldMedicines/getMedicineTypeOnId/',getMedicineTypeOnId,name='getMedicineTypeOnId'),
    path('soldMedicines/getPharmacistOnId/',getPharmacistOnId,name='getPharmacistOnId')
    
=======
    path('viewOrder/',viewOrder,name='viewOrder'),

>>>>>>> e62f9df3ed8bef3fbed98cd72b1f59bd1345f1ff
]