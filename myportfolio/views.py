from django.shortcuts import render
from datetime import datetime
from myportfolio.models import Contact
from .models import Contact
def index(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email,message=message, date = datetime.today())
        contact.save()
    return render(request, 'index.html')
def blog(request):
    return render(request,'blog.html')



 