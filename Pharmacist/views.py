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
            order = addOrder(request,mid,1,quantity)
            return redirect(sellMedicine)

        medicineCode = request.POST.get('medicineCode')
        print(medicineCode)
        medicines = addOrder(request,medicineCode,0)
        print (2222)
        return render(request, "Pharmacist/pharmacist_order_medicine.html", {'medicines': medicines})

      else:
        return render(request, "Pharmacist/pharmacist_order_medicine.html")
    except:
        return render(request, "Pharmacist/pharmacist_order_medicine.html")


def addOrder(request,medicineCode,quantity,order=None):
    pid = request.session.get('id')
    pharmacist = Pharmacist.objects.get(pharmacistId=pid)
    medicines = Medicine.objects.all().filter(medicineId=medicineCode)
    print ('working')
    if order:
        orders = Order(medicine=medicines, pharmacist=pharmacist, quantity=quantity, confirmationState='Pending')
        orders.save()
        return order
    return medicines

def sellMedicine(request):
    return render(request, "Pharmacist/pharmacist_sell_medicine.html")

def medicineStock(request):
    return render(request, "Pharmacist/pharmacist_medicine_stock.html")

def dashboard(request):
    return render(request, "Pharmacist/pharmacist_dashboard.html")