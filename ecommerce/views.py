from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect

from .forms import ContactForm


def home_page(request):
    return render(request,"temp/index.html")

def logout_page(request):
    return render(request,"temp/index.html")



def contact_page(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        # content = request.POST['content']
        # contact_form = request.POST
        # print(contact_form)
        # context = {
        #     "title":"Contact",
        #     "content":" Welcome to the contact page.",
        #     "form": contact_form,
        # }
        # if name.is_valid() and email.is_valid():
            # print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})

        # else:
        #     errors = contact_form.errors.as_json()
        #     if request.is_ajax():
        #         return HttpResponse(errors, status=400, content_type='application/json')

    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "temp/contact.html")

def access(request):
    return render(request,"temp/accessories.html")