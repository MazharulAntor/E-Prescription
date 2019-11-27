from django.shortcuts import render, HttpResponse, redirect

from Patient.views import seePrescription
from Pharmacist.models import Pharmacist
from Doctor.models import Doctor
from Company.models import Company
from Patient.models import Patient
from django.contrib import messages
from Doctor.views import makePrescription
from Pharmacist.views import orderMedicine, afterOrderMedicine


def login(request):

    if request.method == "POST":
        userType = request.POST.get("userType")

        if userType == "Company":
            phoneNumber = request.POST.get("number")
            password = request.POST.get("password")
            company = Company.objects.all().filter(phoneNumber=phoneNumber, password=password)

            for com in company:
                print(com.companyId)
                request.session['id'] = com.companyId
                request.session['userType'] ="company"

            if company:
                return redirect('company/addMedicine/')
            else:
                # return HttpResponse("No Company")
                messages.info(request, 'no company')
                return redirect(login)

        elif userType == "Doctor":
            phoneNumber = request.POST.get("number")
            password = request.POST.get("password")
            doctor = Doctor.objects.all().filter(phoneNumber=phoneNumber, password=password)

            for doc in doctor:
                print(doc.doctorId)
                request.session['id'] = doc.doctorId
                request.session['userType'] ="doctor"
                print(request.session.get('id'))

            if doctor:
                #return render(request, "Doctor/doctor_make_prescription.html", {})
                return redirect(makePrescription)
            else:
                #return HttpResponse("No Doctor")
                messages.info(request, 'no doctor found')
                return redirect(login)
        elif userType == "Pharmacist":
            phoneNumber = request.POST.get("number")
            password = request.POST.get("password")
            pharmacist = Pharmacist.objects.all().filter(phoneNumber=phoneNumber, password=password)

            for phar in pharmacist:
                print(phar.pharmacistId)
                request.session['id'] = phar.pharmacistId

            if pharmacist:
                return redirect(orderMedicine)
            else:
                messages.info(request, 'no pharmacist')
                return redirect(login)

        elif userType == "Patient":
            patientPhoneNumber = request.POST.get("number")
            patientPassword = request.POST.get("password")
            patient = Patient.objects.all().filter(patientPhoneNumber=patientPhoneNumber, patientPassword=patientPassword)

            for pat in patient:
                print(pat.patientId)
                request.session['id'] = pat.patientId
                request.session['userType'] ="patient"
                print(request.session.get('id'))

            if patient:
                return redirect(seePrescription)
            else:
                messages.info(request, 'No user found')
                return redirect(login)

    return render(request, "Account/login.html", {})
