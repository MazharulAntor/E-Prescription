from django.http import HttpResponse
from django.shortcuts import render, redirect

from Company.models import Medicine, MedicineForm, MedicineType, Company


def medicineList(request):
    companyId = request.session.get('id')
    company = Company.objects.get(companyId=companyId)
    medicines = Medicine.objects.all().filter(company=company)

    return render(request, "Company/company medicine list.html",{'medicines': medicines})


def addMedicine(request):
    return render(request, "Company/company_add_medicine.html", {})


def afterAddMedicine(request):

        if request.method == "POST":
            name = request.POST["name"]
            tabletFormId = request.POST["tabletForm"]
            typeId = request.POST["type"]
            quantity = request.POST["quantity"]
            companyId = request.session.get('id')
            company = Company.objects.get(companyId=companyId)
            type=MedicineType.objects.get(medicineTypeId=typeId)
            tabletForm = MedicineForm.objects.get(medicineFormId=tabletFormId)



            addMed=Medicine(company=company, medicineName=name, singleUnitQuantity=quantity, form=tabletForm, type=type)
            addMed.save()
            types = getMedicineType()
            forms = getMedicineForm()

            return render(request, "Company/company_add_medicine.html", {'types': types, 'forms': forms})
        else:
            types = getMedicineType()
            forms = getMedicineForm()

            return render(request, "Company/company_add_medicine.html", {'types': types, 'forms': forms})

def getMedicineType():
    types = MedicineType.objects.all()
    return types

def getMedicineForm():
    forms = MedicineForm.objects.all()
    return forms
