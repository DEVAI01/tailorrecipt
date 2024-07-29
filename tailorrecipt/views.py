from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,redirect
from tailorrecipt import models
from .forms import UserLogin,UserRegister
from . import emailSending
from django.db import IntegrityError
from .models import User,Addcustumer,Upperdetsils,Lowerdetsils,Paymentdetails


curl=settings.CURRENT_URL



def index(request):
    return render(request,"Home.html")

def search(request):
    if request.method=="POST":
        searchid=request.POST.get('searchid')
        print(searchid)
        
        data=models.Addcustumer.objects.filter(Custumerid=searchid).values('Custumer_name','Custumer_mobile','Delivery_date','Custumerid','Update','Current_date')
        print(data)
        data1=models.Upperdetsils.objects.filter(Custumerid_id=searchid).values()
        print(data1)
        data2=models.Lowerdetsils.objects.filter(Custumerid_id=searchid).values()
        print(data2)
        data3=models.Paymentdetails.objects.filter(Custumerid_id=searchid).values()
        print(data3)
        return render(request,'Search.html',{'curl':curl,'context':data,'context1':data1,'context2':data2,'context3':data3,})
    return render(request,'Search.html',{'curl':curl})
    

def login(request):
    
    fm = UserLogin()
    msg=""
    if request.method == "POST":
        fm = UserLogin(request.POST)  
        if fm.is_valid():
            print("Form Validated")
            print("Email:",fm.cleaned_data['email'])
            print("Password:",fm.cleaned_data['password'])
            gemail=fm.cleaned_data['email']
            gpass= fm.cleaned_data['password']
            obj=User.objects.filter(email=gemail,password=gpass)
            
            list = obj.values()
            if len(list) > 0:
                request.session['email'] = gemail 
                print(f'Setting session email: {gemail}')
                if list[0]["role"]=="custumer":
                    return redirect(f'{curl}CustumerApp/custumer')
                elif list[0]["role"]=="user":
                    return redirect(f'{curl}TailorApp/tailorhome')
            else:
                msg="please enter correct credentails"
                return render(request,'Login.html',{'form':fm,'msg':msg})
            
        else:
            return render(request,'Login.html',{'form':fm,'msg':msg})             
            
    elif request.method == "GET":
        return render(request,'Login.html',{"curl":curl,'form':fm})       
            
              
    # sudo systemctl daemon-reload
        

def service(request):
    return render(request,"Service.html",{'curl':curl})


def register(request):
    fm = UserRegister()
    msg=""
    if request.method=="POST":
        fm=UserRegister(request.POST)
        if fm.is_valid():
            print("Form validated")
            print("Name:",fm.cleaned_data['name'])
            print("Email:",fm.cleaned_data['email'])
            print("Password:",fm.cleaned_data['password'])
            print("Mobile:",fm.cleaned_data['mobile'])
            print("Gender:",fm.cleaned_data['gender'])
            print("Date Of Birth:",fm.cleaned_data['dob'])
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            mobile = fm.cleaned_data['mobile']
            gender = fm.cleaned_data['gender']
            dob = fm.cleaned_data['dob']
            Userobj = User(name=name,email=email,password=password,mobile=mobile,gender=gender,dob=dob)
            # for send verification email to registered email id
            
            try:
                Userobj.save()
                msg = "User Registered Successfully"
                emailSending.sendMail(email, password)
            except IntegrityError as e:
                # Check for duplicate entry error
                if '1062' in str(e).split(' ')[0]:
                        msg = "This email address is already registered. Please use a different email."
                else:
                    # Log other integrity errors
                    print(f"IntegrityError occurred: {e}")
                    msg = "User Registration Failed due to an integrity error."
            except Exception as e:
                # Handle other unexpected exceptions
                print(f"An unexpected error occurred: {e}")
                msg = "User Registration Failed."
               
        return render(request,"Register.html",{"curl":curl,"msg":msg,'form':fm})
    elif request.method == "GET":
        return render(request,"Register.html",{"curl":curl,'form':fm})
            
    
    

def contact(request):
    return render(request,"Contact.html",{'curl':curl})








