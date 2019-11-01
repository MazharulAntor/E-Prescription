from django.shortcuts import render, HttpResponse
from Doctor.models import Doctor


def login(request):

    if request.method == "POST":
        userType = request.POST.get("userType")

        if userType == "Doctor":
            phoneNumber = request.POST.get("number")
            password = request.POST.get("password")
            doctor =Doctor.objects.all().filter(phoneNumber=phoneNumber,password=password)

            print (doctor)

            if doctor:
                return render(request, "Doctor/doctor_make_prescription.html", {})
            else:
                return HttpResponse("No Doctor")


    return render(request, "Account/login.html", {})