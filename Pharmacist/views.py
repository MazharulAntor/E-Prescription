from django.shortcuts import render

# Create your views here.
def sellMedicine(request):
    return render(request, "Pharmacist/pharmacist_order_medicine.html")