from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
# Create your views here.
def index(request):
    context={
        "variable":"this is sent"
    }
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, 'index.html')
    #return HttpResponse("This is homepage")

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/home")
        else:
            return render(request,'login.html')
    return render(request, 'login.html')
        

def logoutuser(request):
    logout(request)
    return redirect("/")


def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about")
def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is servicespage")

def contact(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        email=request.POST.get('emailId')
        phoneno=request.POST.get('phoneno')
        textholder=request.POST.get('textholder')
        contact=Contact(name=name, emailId=email,phoneno=phoneno,textholder=textholder,date=datetime.today() )
        contact.save()
        messages.success(request, 'Your message has been delivered.') 
    return render(request, 'contact.html')


def videos(request):
    return render(request,'videos.html')
def delhi(request):
    return render(request,'Delhi.html')
def Mandi(request):
    return render(request,'Mandi.html')
def MSP(request):
    return render(request,'MSP.html')
def Buyers(request):
    return render(request,'Buyers.html')
def rajasthan(request):
    return render(request,'rajasthan.html')
def jodhpur(request):
    return render(request,'jodhpur.html')
def iitjphc(request):
    return render(request,'iitjphc.html')
def hospitals(request):
    return render(request,'hospitals.html')
def appointments(request):
    return render(request,'appointments.html')
def newuser(request):
    if(request.method=='POST'):
        name=request.POST['name']
        emailId=request.POST['emailId']
        Username=request.POST['Username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        # age=request.POST['age']
        # gender=request.POST['gender']
        # Blood=request.POST['Blood']

        myuser=User.objects.create_user(Username,emailId,password)
        myuser.Name= name
        myuser.EmailId= emailId
        myuser.UserName= Username
        myuser.save()
        messages.success(request, "You are successfully registered") 
        return redirect('/home')
    return render(request,'newuser.html')
