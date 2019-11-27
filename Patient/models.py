from django.db import models

# Create your models here.


class PatientSex(models.Model):
    patientSexName = models.CharField(max_length=8,blank=False,null=False)

    def __str__(self):
        return self.patientSexName


class PatientBloodGroup(models.Model):
    patientBloodGroupName = models.CharField(max_length=8, blank=False, null=False)

    def __str__(self):
        return self.patientBloodGroupName


class Patient(models.Model):
    patientId = models.AutoField(primary_key=True)
    patientName = models.CharField(max_length=44, blank=False, null=False)
    patientDateOfBirth = models.DateField(null=False,blank=False)
    patientSex = models.ForeignKey(PatientSex, on_delete=models.CASCADE, default=1, blank=False,null=False)
    patientPhoneNumber = models.CharField(max_length=16, blank=False, null=False)
    patientBloodGroup = models.ForeignKey(PatientBloodGroup, on_delete=models.CASCADE, default=1, blank=False, null=False)
    patientPassword = models.CharField(max_length=33, null=False, blank=False)

    def __str__(self):
        return self.patientName