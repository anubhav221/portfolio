from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        desc = request.POST['desc']
    
        contact=Contact.objects.create(name=name, phone=phone, email=email, desc=desc)
        messages.success(request, 'Your message has been sumbitted.')
        # desc.success(request,'Data has been submitted')
    return render(request, 'index.html')