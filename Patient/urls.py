from django.urls import path
from Patient.views import seePrescription

urlpatterns = [

    path('seePrescription/', seePrescription, name="seePrescription"),
    
]