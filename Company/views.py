from django.http import HttpResponse
from django.shortcuts import render

from Company.models import Medicine, MedicineForm, MedicineType, Company


def addMedicine(request):
    return render(request, "Company/company_add_medicine.html", {})

def afterAddMedicine(request):
        if request.method == "POST":
            name = request.post.get("name")
            tabletForm = request.post.get("tabletForm")
            type = request.post.get("type")
            quantity = request.post.get("quantity")

            addMed=Medicine(companyId="01620281268", medicineName=name, singleUnitQuantity=quantity, formId=tabletForm, typeId=type)
            addMed.save()
        else:
            types = MedicineType.objects.all()
            forms = MedicineForm.objects.all()

            return render(request, "Company/company_add_medicine.html", {'types': types, 'forms': forms})
