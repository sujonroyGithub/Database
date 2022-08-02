import email
from django.shortcuts import render
from datetime import datetime
from home.models import Contact,Help
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        title = request.POST.get('title')
        salary = request.POST.get('salary')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        presentaddress = request.POST.get('presentaddress')
        desc = request.POST.get('desc')
        agree= request.POST.get('agree')
        
        contact = Contact(name=name,title=title,salary=salary,email=email,phone=phone,address=address,presentaddress=presentaddress,desc=desc,agree=agree,date=datetime.today())
        contact.save()
        messages.success(request, ' Your Information Has been Sent Sucessfully..')
    return render(request,'contact.html')

def help(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        help = Help(name=name,email=email,message=message,date=datetime.today())
        help.save()
        messages.success(request, ' Your Message Has been Sent Sucessfully..We will check in 2 days')
    return render(request, 'help.html')

def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')    