from django.http import HttpResponse
from django.shortcuts import render, redirect

from Company.models import Medicine, MedicineForm, MedicineType, Company
from Pharmacist.models import Order, Pharmacist, MedicineStock

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


def viewOrder(request):
    cid = request.session.get('id')
    company = Company.objects.get(companyId=cid)
    orders = Order.objects.all().filter(company=company)
    if request.POST.get('update'):
        status = request.POST.get('status')
        date = request.POST.get('date')
        orderId = int(request.POST.get('orderId'))
        medId = int(request.POST.get('medId'))
        medicine = Medicine.objects.get(medicineId=medId)
        pharId = int(request.POST.get('pharId'))
        quantity = int(request.POST.get('quantity'))
        pharmacist=Pharmacist.objects.get(pharmacistId=pharId)
        medicineStocks=MedicineStock.objects.all().filter(pharmacist=pharmacist)
        stop=0
        if status=="Accepted":
            for order in orders:
                if order.orderId == orderId:
                    if order.confirmationState != "Delivered":
                      order.confirmationState=status
                      order.deliveryDate = date
                      order.save()
        if status=="Delivered":
            for order in orders:
                if order.orderId == orderId:
                    if order.confirmationState != "Delivered":
                       order.confirmationState=status
                       order.deliveryDate = date
                       order.save()
                       for medicineStock in medicineStocks:
                           if medicineStock.medicine.medicineId == medId:
                               existQuantity=medicineStock.quantity
                               quantity=quantity+existQuantity
                               medicineStock.quantity=quantity
                               medicineStock.save()
                               stop=1
                       if stop!=1:
                        medicineStock=MedicineStock(medicine=medicine,pharmacist=pharmacist,quantity=quantity)
                        medicineStock.save()


    return render(request, "Company/company_view_order.html", {'orders': orders})

