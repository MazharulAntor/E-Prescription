from django.urls import path
from .views import makePrescription,getPatientsPhoneNumber,getPatientsNameOnPhoneNumber


urlpatterns = [
    path('makePrescription/', makePrescription, name="makePrescription"),
    path('makePrescription/getPatientPhoneNumber/', getPatientsPhoneNumber, name="getPatientPhoneNumber"),
    path('makePrescription/getPatientsNameOnPhoneNumber/', getPatientsNameOnPhoneNumber, name="getPatientsNameOnPhoneNumber"),

]