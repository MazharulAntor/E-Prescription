from django.contrib import admin

# Register your models here.
from Patient.models import Patient, PatientBloodGroup, PatientSex

admin.site.register(Patient)
admin.site.register(PatientSex)
admin.site.register(PatientBloodGroup)
