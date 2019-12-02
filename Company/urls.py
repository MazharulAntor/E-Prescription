from django.urls import path

from .views import addMedicine, getAddMedicinePage, medicineList, viewOrder

urlpatterns = [
    path('addMedicine/', getAddMedicinePage, name="addmedicine"),
    path('medicineList/',medicineList,name='medicineList'),
    path('viewOrder/',viewOrder,name='viewOrder'),

]