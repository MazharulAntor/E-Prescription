from django.contrib import admin
from .models import PatientSex, PatientBloodGroup, Patient, Prescription, PrescribedMedicine

admin.site.register(PatientSex)
admin.site.register(PatientBloodGroup)
admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(PrescribedMedicine)
