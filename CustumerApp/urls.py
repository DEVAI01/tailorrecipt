# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import bookings, download_receipt 

app_name = 'CustumerApp' 

urlpatterns = [
    path('custumer/', views.custumer, name='custumer'),
    path('services/', views.services),
    path('bookings/', views.bookings),
    path('chatus/', views.chatus),
    path('custumersettings/', views.custumersettings),
    path('logout/', views.logout, name='logout'),
    path('download_receipt/<int:booking_id>/', views.download_receipt, name='download_receipt'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
