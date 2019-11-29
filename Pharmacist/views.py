from django.shortcuts import render, redirect
from Company.models import Medicine
from Pharmacist.models import Pharmacist, MedicineStock, Order
from django.utils import timezone

def orderMedicine(request):
    try:
      if request.method == "POST":

        if request.POST.get('quantity'):
            quantity=request.POST.get('quantity')
            print(quantity)
            mid = request.POST.get('mid')
            addOrder(request,mid,quantity,1)
            return redirect(myOrders)

        medicineCode = request.POST.get('medicineCode')
        medicines = addOrder(request,medicineCode,0)
        return render(request, "Pharmacist/pharmacist_order_medicine.html", {'medicines': medicines})

      else:
        return render(request, "Pharmacist/pharmacist_order_medicine.html")
    except:
        return render(request, "Pharmacist/pharmacist_order_medicine.html")


def addOrder(request,medicineCode,quantity,order=None):
    pid = request.session.get('id')
    pharmacist = Pharmacist.objects.get(pharmacistId=pid)
    mediciness = Medicine.objects.get(medicineId=medicineCode)
    medicines = Medicine.objects.all().filter(medicineId=medicineCode)

    if order:
        print ('Before order')
        orders = Order(medicine=mediciness, pharmacist=pharmacist, quantity=quantity, confirmationState='Pending')
        orders.save()
        print('After order')
        return order
    return medicines

def sellMedicine(request):
    return render(request, "Pharmacist/pharmacist_sell_medicine.html")

def medicineStock(request):
    pid = request.session.get('id')
    pharmacists = Pharmacist.objects.get(pharmacistId=pid)
    medicineStocks = MedicineStock.objects.all().filter(pharmacist=pharmacists)
    return render(request, "Pharmacist/pharmacist_medicine_stock.html", {'medicineStocks': medicineStocks})

def dashboard(request):
    return render(request, "Pharmacist/pharmacist_dashboard.html")

def myOrders(request):
    pid = request.session.get('id')
    pharmacists = Pharmacist.objects.get(pharmacistId=pid)
    orders = Order.objects.all().filter(pharmacist=pharmacists)
    return render(request, "Pharmacist/pharmacist_my_order_list.html", {'orders': orders})