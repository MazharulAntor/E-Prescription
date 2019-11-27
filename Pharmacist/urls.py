from django.urls import path

from Pharmacist.views import orderMedicine, medicineStock, sellMedicine, dashboard

urlpatterns = [
    path('orderMedicine/', orderMedicine, name='orderMedicine'),
    path('sellMedicine/', sellMedicine, name='sellMedicine'),
    path('medicineStock/', medicineStock, name='medicineStock'),
    path('dashboard/', dashboard, name='dashboard'),
]