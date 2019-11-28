from django.shortcuts import render, redirect
from Company.models import Medicine
from Pharmacist.models import Pharmacist, Order

def orderMedicine(request):
    try:
      if request.method == "POST":

        if request.POST.get('quantity'):
            quantity=request.POST.get('quantity')
            print(quantity)
            mid = request.POST.get('mid')
            order = addOrder(request,mid,quantity,1)
            return redirect(sellMedicine)

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
    medicines = Medicine.objects.all().filter(medicineId=medicineCode)

    if order:
        print ('Before order')
        orders = Order(medicine=medicines, pharmacist=pharmacist, quantity=quantity, confirmationState='Pending')
        orders.save()
        print (pharmacist.storeName)
        return order
    return medicines

def sellMedicine(request):
    return render(request, "Pharmacist/pharmacist_sell_medicine.html")

def medicineStock(request):
    pid = request.session.get('id')
    print (pid)
    pharmacists = Pharmacist.objects.all().filter(pharmacistId=pid)
    print (pharmacists)
    return render(request, "Pharmacist/pharmacist_medicine_stock.html", {'pharmacists': pharmacists})

def dashboard(request):
    return render(request, "Pharmacist/pharmacist_dashboard.html")