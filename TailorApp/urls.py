from django.urls import path
from . import views
from django.conf.urls.static import static
from .views import invoice
# Create your views here.

app_name = 'TailorApp' 

urlpatterns=[

    path('tailorhome/',views.tailorhome,name='tailorhome'),
    path('editsdeatils/',views.editsdeatils),
    path('upgradeprogress/',views.upgradeprogress),
    path('searching/',views.searching),
    path('Settingshome/',views.Settingshome),
    path('logout/',views.logout),
    path('addclothes/',views.addclothes),
    path('uppersinglecloth/',views. uppersinglecloth),
    path('coupleclothes/',views.coupleclothes),
    path('invoice/', invoice, name='invoice'),
    path('doublecoupleclothes/',views.doublecoupleclothes),
    path('lowersinglecloth/',views.lowersinglecloth),
    path('tripleclothes/',views.tripleclothes),
    path('user/',views.user),
    path('approved/',views.approved),
    path('password/',views.password),
    path('dueview/',views.dueview),
    path('idinvoice/',views.idinvoice),
    path('custumerlist/',views.custumerlist),
    path('deletedue/',views.deletedue),
    path('deleteitemu/',views.deleteitemu),
    path('deleteiteml/',views.deleteiteml),
    path('deleteuser/',views.deletecustumer),
    path('filter/',views.filter),
    path('bookings/',views.bookings),
    path('QRCODE',views.QRCODE),

    
    
    
]