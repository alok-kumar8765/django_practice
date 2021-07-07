from django.core.checks import messages
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import  messages

# Create your views here.
def index(request):
    context={
        "variable1":"this is var 1 sent",
        "variable2":"this is var 2 sent"
    }
    #just t check message show as variable 
    #messages.success(request,"this is a test message")
    return render(request,'index.html',context)
    #return HttpResponse('index page')
def about(request):
    return render(request,'about.html')
    #return HttpResponse('about page')
def services(request):
    return render(request,'services.html')
    #return HttpResponse('services page')
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        query=request.POST.get('query')
        contact=Contact(name=name,email=email,phone=phone,query=query,date=datetime.today())
        contact.save()
        messages.success(request,'Data Saved')
    return render(request,'contact.html')
    #return HttpResponse('contact page')