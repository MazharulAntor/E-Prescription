from django.db import models

class Pharmacist(models.Model):
    storeName = models.CharField(max_length=25, blank=False, null=False)
    licence = models.CharField(max_length=50, blank=False, null=False)
    phoneNumber = models.CharField(max_length=50, blank=False, null=False)
    storeAddress = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return self.phoneNumber
