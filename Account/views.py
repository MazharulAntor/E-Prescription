from django.shortcuts import render, HttpResponse, redirect
from Doctor.models import Doctor
from Company.models import Company
from Patient.models import Patient
from django.contrib import messages



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
                print(request.session.get('id'))

            if doctor:
                return render(request, "Doctor/doctor_make_prescription.html", {})
            else:
                #return HttpResponse("No Doctor")
                messages.info(request, 'no doctor found')
                return redirect(login)

    return render(request, "Account/login.html", {})
