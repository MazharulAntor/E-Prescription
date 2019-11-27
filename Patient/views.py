from django.shortcuts import render

# Create your views here.
def seePrescription(request):

    return render(request, "Patient/patient_prescription.html")