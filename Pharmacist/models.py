from django.db import models

# Create your models here.


class Pharmacist(models.Model):
    pharmacistId = models.AutoField(primary_key=True)
    pharmacistStoreName = models.CharField(max_length=33,blank=False,null=False)
    pharmacistDrugLicence = models.CharField(max_length=33,blank=False, null=False)
    pharmacistPhoneNummber = models.BigIntegerField(max_length=18, null=False, blank=False)
    pharmacistStoreAddress = models.CharField(max_length=33,null=False, blank=False)
    pharmacistPassword = models.CharField(max_length=33,blank=False,null=False)

    def __str__(self):
        return self.pharmacistStoreName