# views.py
from django.shortcuts import render,redirect
from django.conf import settings


curl = settings.CURRENT_URL
media_url = settings.MEDIA_URL

def custumer(request):
    email = request.session.get('email', 'Guest')
    msg = 'Thanks for chossing us'
    print(email)
    return render(request, 'CustumerHome.html', {'curl': curl, 'msg': msg, 'email': email})
# def bookings(request):
#     msg = ''
#     email = request.session.get('email', 'Guest')
#     print(email)
#     return render(request, 'Bookings.html', {'curl': curl, 'msg': msg, 'email': email})

def bookings(request):
    msg = ''
    email = request.session.get('email', 'Guest')
    
    if request.method == 'POST':
        upper_wear = request.POST.getlist('upper_wear')
        lower_wear = request.POST.getlist('lower_wear')
        description = request.POST.get('description')
        
        print("Upper Wear: ", upper_wear)
        print("Lower Wear: ", lower_wear)
        print("Description: ", description)
        
        # Here you can handle the form data (e.g., save to the database, send an email, etc.)
        msg = 'Form submitted successfully!'
        
    return render(request, 'Bookings.html', {'curl': curl, 'msg': msg, 'email': email})

def chatus(request):
    email = request.session.get('email', 'Guest')
    msg = ''
    print(email)
    return render(request, 'Chatus.html', {'curl': curl, 'msg': msg, 'email': email})
    
def custumersettings(request):
    msg = ''
    email = request.session.get('email', 'Guest')
    print(email)
    return render(request, 'Settings.html', {'curl': curl, 'msg': msg, 'email': email})

    
def services(request):
    msg = ''
    email = request.session.get('email', 'Guest')
    print(email)
    return render(request, 'Services.html', {'curl': curl, 'msg': msg, 'email': email})



def some_protected_view(request):
    if 'email' not in request.session:
        return redirect('login')
    # ... rest of your view code ...
    
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

def logout(request):
    auth_logout(request)
    request.session.flush()
    return redirect('index')