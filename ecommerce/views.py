from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist

from .forms import ContactForm
from .models import Contact
from orders.models import Order

def home_page(request):
    return render(request,"temp/index.html")

def logout_page(request):
    return render(request,"temp/index.html")

def conditions_page(request):
    return render(request,"temp/TAC.html")

def policy(request):
    return render(request,"temp/policy.html")



def contact_page(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        order_id = request.POST['order_id']
        message = request.POST['message']
        try:
            order_obj = Order.objects.get(order_id=order_id)
            if email != order_obj.billing_profile.email:
                messages.error(self.request, "Email does not match for the given OrderId.")
                return redirect("contact")
            contact = Contact()
            contact.username = name
            contact.email = email
            contact.order_id = order_id
            contact.message = message
            contact.save()
            if request.is_ajax():
                return JsonResponse({"message": "Thank you for your submission"})
                
        except ObjectDoesNotExist:
                # messages.error(self.request, "This order does not exist.")
                if request.is_ajax():
                    return JsonResponse({"message": "This order does not exist"})
                return redirect("contact")
        
    return render(request, "temp/contact.html")

def access(request):
    return render(request,"temp/accessories.html")