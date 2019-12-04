from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect

from Company.models import Medicine, MedicineForm, MedicineType, Company, AntibioticType
from Pharmacist.models import Pharmacist
from Pharmacist.models import SoldMedicineWithoutPrescription,Pharmacist
from django.core import serializers
from Account.views import login
from django.db.models import Q



def getSoldMedicinesPage(request):
    companyId = request.session.get('id')
    userType = request.session.get('userType')
    print("type")
    print(userType)
    if 'userType' not in request.session:
        return redirect(login)
    if 'id' not in request.session:
        return redirect(login)
    if userType!="company":
        return redirect(login)
    
    antibioticTypes = AntibioticType.objects.all()
    
    #antibioticTypeJson = serializers.serialize("json",antibioticType)
    return render(request, "Company/company_sold_medicine.html",{"antibioticTypes": antibioticTypes})

def getSoldMedicineWithoutPrescription(request):
    if request.method=="GET":
        medicineType = request.GET['medicineType']
        if medicineType=="Non-Antibiotic":
            soldMedicineWithoutPrescription = SoldMedicineWithoutPrescription.objects.filter(medicine__type__antibioticType__antibioticTypeId="1")
            #soldMedicineWithoutPrescription= SoldMedicineWithoutPrescription.objects.raw("select * from pharmacist_SoldMedicineWithoutPrescription inner join company_medicine on pharmacist_SoldMedicineWithoutPrescription.medicine_id=company_medicine.medicineId inner join company_medicinetype on company_medicine.type_id=company_medicinetype.medicineTypeId inner join company_antibiotictype on company_medicinetype.antibioticType_id=company_antibiotictype.antibioticTypeId where company_antibiotictype.antibioticTypeName='"+medicineType+"'")
            for s in soldMedicineWithoutPrescription:
                print(s.quantity)
            soldMedicineWithoutPrescriptionJson=serializers.serialize("json",soldMedicineWithoutPrescription)
            
            return JsonResponse({"soldMedicineWithoutPrescription":soldMedicineWithoutPrescriptionJson})

def getMedicineOnId(request):
    if request.method=="GET":
        medicineId= request.GET['medicineId']
        medicine = Medicine.objects.filter(medicineId=medicineId)
        for s in medicine:
                print(s.medicineName)
        medicineJson = serializers.serialize("json",medicine)
        return JsonResponse({"medicine": medicineJson})

def getMedicineTypeOnId(request):
    if request.method=="GET":
        medicineTypeId= request.GET['medicineTypeId']
        medicineType = MedicineType.objects.filter(medicineTypeId=medicineTypeId)
        medicineTypeJson = serializers.serialize("json",medicineType)
        return JsonResponse({"medicineType": medicineTypeJson})

def getPharmacistOnId(request):
    if request.method=="GET":
        pharmacistId = request.GET['pharmacistId']
        pharmacist = Pharmacist.objects.filter(pharmacistId=pharmacistId)
        pharmacistJson = serializers.serialize("json",pharmacist)
        return JsonResponse({"pharmacist": pharmacistJson})



def medicineList(request):
    companyId = request.session.get('id')
    userType = request.session.get('userType')
    print("type")
    print(userType)
    if 'userType' not in request.session:
        return redirect(login)
    if 'id' not in request.session:
        return redirect(login)
    if userType!="company":
        return redirect(login)
    companyId = request.session.get('id')
    company = Company.objects.get(companyId=companyId)
    medicines = Medicine.objects.all().filter(company=company)

    return render(request, "Company/company medicine list.html",{'medicines': medicines})


def addMedicine(request):
    return render(request, "Company/company_add_medicine.html", {})


def getAddMedicinePage(request):
        companyId = request.session.get('id')
        userType = request.session.get('userType')
        print("type")
        print(userType)
        if 'userType' not in request.session:
            return redirect(login)
        if 'id' not in request.session:
            return redirect(login)
        if userType!="company":
            return redirect(login)

        if request.method == "POST":
            name = request.POST["name"]
            tabletFormId = request.POST["tabletForm"]
            typeId = request.POST["type"]
            quantity = request.POST["quantity"]
            
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
