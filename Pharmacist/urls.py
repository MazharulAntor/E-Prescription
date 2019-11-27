from django.urls import path

from Pharmacist.views import orderMedicine, afterOrderMedicine

urlpatterns = [
    path('orderMedicine/', orderMedicine, name="orderMedicine"),
    path('orderMedicine/afterOrderMedicine/', afterOrderMedicine, name="afterOrderMedicine"),
]