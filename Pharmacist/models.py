from django.db import models

from Company.models import Company, Medicine


class Pharmacist(models.Model):
    pharmacistId = models.AutoField(primary_key=True)
    storeName = models.CharField(max_length=33,blank=False,null=False)
    drugLicence = models.CharField(max_length=33, blank=False, null=False)
    phoneNumber = models.CharField(max_length=18, null=False, blank=False)
    storeAddress = models.CharField(max_length=33,null=False, blank=False)
    password = models.CharField(max_length=33,blank=False,null=False)

    def __str__(self):
        return self.storeName

class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    pharmacist = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50, blank=False, null=False)
    confirmationState = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.confirmationState

class MedicineStock(models.Model):
    medicineStockId = models.AutoField(primary_key=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    pharmacist = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50, blank=False, null=False)

    def __int__(self):
        return self.medicineStockId