from django.urls import path

from Pharmacist.views import sellMedicine

urlpatterns = [
    path('sellMedicine/', sellMedicine, name="sellMedicine"),

]