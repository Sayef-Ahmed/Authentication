from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.home import Admin, LOGIN, LOGOUT, AD_REGISTRATION

app_name = 'admin_dashbord'

urlpatterns = [
    path('', Admin, name='dashbord'),
    path('accounts/login/', LOGIN, name='login'),
    path('logout', LOGOUT, name='logout'),
    path('accounts/admin/registration/', AD_REGISTRATION, name='ad_registration'),

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)