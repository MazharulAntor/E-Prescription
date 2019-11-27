from django.shortcuts import render

# Create your views here.
from Company.models import Medicine
from Pharmacist.models import Pharmacist, Order


def orderMedicine(request):


    return render(request, "Pharmacist/pharmacist_order_medicine.html")

def afterOrderMedicine(request):
    if request.method == "GET":
        medicineCode = request.GET.get('medicineCode')
        pharmacistId = request.session.get('id')
        pharmacist = Pharmacist.objects.get(pharmacistId=pharmacistId)
        medicines = Medicine.objects.all().filter(medicineId=1)
        print(medicineCode)
        orders = Order.objects.all()
        return render(request, "Pharmacist/pharmacist_order_medicine.html", {'medicines': medicines})
    else:
        return render(request, "Pharmacist/pharmacist_order_medicine.html")



