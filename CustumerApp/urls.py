# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'CustumerApp' 

urlpatterns = [
    path('custumer/', views.custumer, name='custumer'),
    path('services/', views.services),
    path('bookings/', views.bookings),
    path('chatus/', views.chatus),
    path('custumersettings/', views.custumersettings),
    path('logout/', views.logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
