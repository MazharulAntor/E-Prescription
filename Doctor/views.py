from django.shortcuts import render
from Patient.models import Patient,PatientBloodGroup, PatientSex
from Company.models import Company, Medicine, MedicineType
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

def makePrescription(request):
    patientBloodGroup = PatientBloodGroup.objects.all()
    companys = Company.objects.values('companyId','name').order_by('name')
    medicineTypes = MedicineType.objects.values('medicineTypeId','medicineTypeName').order_by('medicineTypeName')
    patientSexes = PatientSex.objects.all()
    for pa in medicineTypes:
            print(pa)
    return render(request, "Doctor/doctor_make_prescription.html", {'patientBloodGroup': patientBloodGroup,'companys': companys, 'medicineTypes': medicineTypes, 'patientSexes': patientSexes})

def getPatientsPhoneNumber(request):
    if request.method=="GET":
        
        patientPhoneNumber = Patient.objects.all()
        for pa in patientPhoneNumber:
            print(pa)
        SomeModel_json = serializers.serialize("json", patientPhoneNumber,fields=('patientPhoneNumber'))
        
    return JsonResponse({'patientPhoneNumber' : SomeModel_json})

def getPatientsNameOnPhoneNumber(request):
    if request.method=="GET":
        patientPhoneNumber = request.GET['patientPhoneNumber']
        patientName = Patient.objects.filter(patientPhoneNumber=patientPhoneNumber)
        for pa in patientName:
            print(pa.patientName)
        SomeModel_json = serializers.serialize("json", patientName,fields=('patientName'))
    return JsonResponse({'patientName': SomeModel_json})

def getPatientOnNameAndPhoneNumber(request):
    if request.method=="GET":
        patientName = request.GET['patientName']
        patientPhoneNumber = request.GET['patientPhoneNumber']
        patient = Patient.objects.filter(patientName=patientName,patientPhoneNumber=patientPhoneNumber)
        for pa in patient:
            print("sex")
            print(pa.patientDateOfBirth)
        
        SomeModel_json = serializers.serialize("json", patient,fields=('patientId', 'patientName','patientDateOfBirth','patientSex','patientBloodGroup','patientPhoneNumber'))
        return JsonResponse({'patient': SomeModel_json})

def getMedicineOnType(request):
    if request.method=="GET":
        medicineTypeId = request.GET['medicineTypeId']
        medicine = Medicine.objects.filter(type=medicineTypeId)
        medicineInJson = serializers.serialize("json",medicine,fields=('medicineId','medicineName'))
        return JsonResponse({"medicine": medicineInJson})

def getMedicineOnCompany(request):
    if request.method=="GET":
        medicineCompanyId = request.GET['medicineCompanyId']
        medicine = Medicine.objects.filter(company=medicineCompanyId)
        for pa in medicine:
            print(pa.medicineId)
        medicineInJson = serializers.serialize("json",medicine,fields=('medicineId','medicineName'))
        return JsonResponse({"medicine": medicineInJson})

def getMedicineOnCompanyAndType(request):
    if request.method=="GET":
        medicineCompanyId = request.GET['medicineCompanyId']
        medicineTypeId = request.GET['medicineTypeId']
        medicine = Medicine.objects.filter(type=medicineTypeId,company=medicineCompanyId)
        medicineInJson = serializers.serialize("json",medicine,fields=('medicineId','medicineName'))
        return JsonResponse({"medicine": medicineInJson})
