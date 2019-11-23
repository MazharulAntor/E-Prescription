from django.shortcuts import render
from Patient.models import Patient,PatientBloodGroup
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

def makePrescription(request):
    patientBloodGroup = PatientBloodGroup.objects.all()
    for pa in patientBloodGroup:
            print(pa)
    return render(request, "Doctor/doctor_make_prescription.html", {'patientBloodGroup': patientBloodGroup})

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
        patientName = request.POST['patientName']
        patientPhoneNumber = request.POST['patientPhoneNumber']
        patient = Patient.objects.filter(patientName=patientName,patientPhoneNumber=patientPhoneNumber).values('patientId', 'patientName','patientDateOfBirth','patientSex','patientBloodGroup','patientPhoneNumber')
        patientJsonData = {
            'patient': patient 
        }
        return JsonResponse(patientJsonData)

