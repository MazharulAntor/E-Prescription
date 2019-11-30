from django.urls import path
from .views import addMedicine, getAddMedicinePage, medicineList

urlpatterns = [
    path('addMedicine/', getAddMedicinePage, name="addmedicine"),
    path('medicineList/',medicineList,name='medicineList')
]