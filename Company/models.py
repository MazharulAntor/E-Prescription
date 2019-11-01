from django.db import models

medicine_type = (
    ("MA'S", "MA'S"),
    ("CTS", "CTS")
)


class Company(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    licence = models.CharField(max_length=50, blank=False, null=False)
    phoneNumber = models.CharField(max_length=15, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    #company = models.ForeignKey(Company, on_delete=models.CASCADE)
    companyNumber = models.CharField(max_length=11, blank=False, null=False)
    medicineName = models.CharField(max_length=25, blank=False, null=False)
    singleUnitQuantity = models.CharField(max_length=50, blank=False, null=False)
    formName = models.CharField(max_length=15,choices=medicine_type, blank=False, null=False)
    type = models.CharField(max_length=15, choices=medicine_type, blank=False, null=False)

    def __str__(self):
        return "{0},{1}".format(self.companyNumber,self.medicineName)


