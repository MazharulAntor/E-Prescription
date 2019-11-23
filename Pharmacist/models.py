from django.db import models

# Create your models here.


class Pharmacist(models.Model):
    pharmacistId = models.AutoField(primary_key=True)
    storeName = models.CharField(max_length=33,blank=False,null=False)
    drugLicence = models.CharField(max_length=33, blank=False, null=False)
    phoneNumber = models.CharField(max_length=18, null=False, blank=False)
    storeAddress = models.CharField(max_length=33,null=False, blank=False)
    password = models.CharField(max_length=33,blank=False,null=False)

    def __str__(self):
        return self.storeName