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
    
from django.contrib.auth.hashers import check_password

# def login(request):
#     fm = UserLogin()
#     msg = ""
#     if request.method == "POST":
#         fm = UserLogin(request.POST)
#         if fm.is_valid():
#             print("Form Validated")
#             print("Email:", fm.cleaned_data['email'])
#             print("Password:", fm.cleaned_data['password'])
#             gemail = fm.cleaned_data['email']
#             gpass = fm.cleaned_data['password']
            
#             try:
#                 # Retrieve user by email
#                 user = User.objects.get(email=gemail)
                
#                 # Check if the password matches
#                 if check_password(gpass, user.password):
#                     request.session['email'] = gemail
#                     print(f'Setting session email: {gemail}')
                    
#                     if user.role == "custumer":
#                         return redirect(f'{curl}CustumerApp/custumer')
#                     elif user.role == "user":
#                         return redirect(f'{curl}TailorApp/tailorhome')
#                 else:
#                     msg = "Please enter correct credentials"
                    
#             except User.DoesNotExist:
#                 # Handle case where the user does not exist
#                 msg = "Please enter correct credentials"
            
#         return render(request, 'Login.html', {'form': fm, 'msg': msg})
    
#     elif request.method == "GET":
#         return render(request, 'Login.html', {"curl": curl, 'form': fm})



# def login(request):
#     fm = UserLogin()
#     msg = ""
#     if request.method == "POST":
#         fm = UserLogin(request.POST)
#         if fm.is_valid():
#             print("Form Validated")
#             gemail = fm.cleaned_data['email']
#             gpass = fm.cleaned_data['password']
#             try:
#                 # Get user by email
#                 obj = User.objects.get(email=gemail)
#                 print(obj)
                
#                 if gpass == obj.password:
#                     request.session['email'] = gemail
#                     request.session['user_id'] = obj.userid
                    
                   
#                     print(f'Setting session email: {gemail}')
                    
#                     # Check user role and redirect accordingly
#                     if obj.role == "custumer":
#                         return redirect(f'{curl}CustumerApp/custumer')
#                     elif obj.role == "user":
#                         return redirect(f'{curl}TailorApp/tailorhome')
#                     else:
#                         msg = "Invalid role assigned to user"
#                 else:
#                     # Password didn't match
#                     msg = "Incorrect password"
#             except User.DoesNotExist:
#                 # User with provided email doesn't exist
#                 msg = "User does not exist"
#     elif request.method == "GET":
#         return render(request, 'Login.html', {"curl": curl, 'form': fm})

#     # In case of failure, render login page with message
#     return render(request, 'Login.html', {'form': fm, 'msg': msg})

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import check_password

def login(request):
    fm = UserLogin()
    msg = ""
    if request.method == "POST":
        fm = UserLogin(request.POST)
        if fm.is_valid():
            gemail = fm.cleaned_data['email']
            gpass = fm.cleaned_data['password']
            try:
                obj = User.objects.get(email=gemail)
                
                # Check if the provided password matches the hashed password in the database
                if check_password(gpass, obj.password):
                    request.session['email'] = gemail
                    request.session['user_id'] = obj.userid
                    
                    # Get the 'next' parameter or use a default
                    next_url = request.GET.get('next', reverse('index'))
                    
                    # Redirect based on user role
                    if obj.role == "custumer":
                        return redirect(next_url if next_url != reverse('index') else reverse('CustumerApp:custumer'))
                    elif obj.role == "user":
                        return redirect(next_url if next_url != reverse('index') else reverse('TailorApp:tailorhome'))
                    else:
                        msg = "Invalid role assigned to user"
                else:
                    msg = "Incorrect password"
            except User.DoesNotExist:
                msg = "User does not exist"
    
    # For GET requests or failed logins
    next_url = request.GET.get('next', '')
    return render(request, 'Login.html', {"curl": curl, 'form': fm, 'msg': msg, 'next': next_url})
   
              
    # sudo systemctl daemon-reload
def service(request):
    return render(request,"Service.html",{'curl':curl})

from django.contrib.auth.hashers import make_password

# def register(request):
#     fm = UserRegister()
#     msg=""
#     if request.method=="POST":
#         fm=UserRegister(request.POST)
#         if fm.is_valid():
#             print("Form validated")
#             print("Name:",fm.cleaned_data['name'])
#             print("Email:",fm.cleaned_data['email'])
#             print("Password:",fm.cleaned_data['password'])
#             print("Mobile:",fm.cleaned_data['mobile'])
#             print("Gender:",fm.cleaned_data['gender'])
#             print("Date Of Birth:",fm.cleaned_data['dob'])
#             name = fm.cleaned_data['name']
#             email = fm.cleaned_data['email']
#             password = fm.cleaned_data['password']
#             mobile = fm.cleaned_data['mobile']
#             gender = fm.cleaned_data['gender']
#             dob = fm.cleaned_data['dob']
#             Userobj = User(name=name,email=email,password=password,mobile=mobile,gender=gender,dob=dob)
#             # for send verification email to registered email id
            
#             try:
#                 Userobj.save()
#                 msg = "User Registered Successfully"
#                 emailSending.sendMail(email, password)
#             except IntegrityError as e:
#                 # Check for duplicate entry error
#                 if '1062' in str(e).split(' ')[0]:
#                         msg = "This email address is already registered. Please use a different email."
#                 else:
#                     # Log other integrity errors
#                     print(f"IntegrityError occurred: {e}")
#                     msg = "User Registration Failed due to an integrity error."
#             except Exception as e:
#                 # Handle other unexpected exceptions
#                 print(f"An unexpected error occurred: {e}")
#                 msg = "User Registration Failed."
               
#         return render(request,"Register.html",{"curl":curl,"msg":msg,'form':fm})
#     elif request.method == "GET":
#         return render(request,"Register.html",{"curl":curl,'form':fm})
 
def register(request):
    fm = UserRegister()
    msg = ""
    if request.method == "POST":
        fm = UserRegister(request.POST)
        if fm.is_valid():
            print("Form validated")
            print("Name:", fm.cleaned_data['name'])
            print("Email:", fm.cleaned_data['email'])
            print("Password:", fm.cleaned_data['password'])
            print("Mobile:", fm.cleaned_data['mobile'])
        
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            mobile = fm.cleaned_data['mobile']
     
            
            # Hash the password before saving
            hashed_password = make_password(password)
            
            Userobj = User(name=name, email=email, password=hashed_password, mobile=mobile)
            
            # For sending a verification email to the registered email ID
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
            
        return render(request, "Register.html", {"curl": curl, "msg": msg, 'form': fm})
    elif request.method == "GET":
        return render(request, "Register.html", {"curl": curl, 'form': fm})
           
    
    

def contact(request):
    return render(request,"Contact.html",{'curl':curl})


from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout as auth_logout


def logout_view(request):
    auth_logout(request)
    request.session.flush()
    return redirect('index')

