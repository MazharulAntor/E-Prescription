from django.urls import path
from .views import makePrescription,getPatientsPhoneNumber,getPatientsNameOnPhoneNumber,getPatientOnNameAndPhoneNumber,getMedicineOnType,getMedicineOnCompany,getMedicineOnCompanyAndType


urlpatterns = [
    path('makePrescription/', makePrescription, name="makePrescription"),
    path('makePrescription/getPatientPhoneNumber/', getPatientsPhoneNumber, name="getPatientPhoneNumber"),
    path('makePrescription/getPatientsNameOnPhoneNumber/', getPatientsNameOnPhoneNumber, name="getPatientsNameOnPhoneNumber"),
    path('makePrescription/getPatientOnNameAndPhoneNumber/', getPatientOnNameAndPhoneNumber, name="getPatientOnNameAndPhoneNumber"),
    path('makePrescription/getMedicineOnType/', getMedicineOnType, name="getMedicineOnType"),
    path('makePrescription/getMedicineOnCompany/', getMedicineOnCompany, name="getMedicineOnCompany"),
    path('makePrescription/getMedicineOnCompanyAndType/', getMedicineOnCompanyAndType, name="getMedicineOnCompanyAndType"),

]