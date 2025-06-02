from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.home import HOME, LOGIN, LOGOUT, CU_REGISTRATION, AD_REGISTRATION, ED_REGISTRATION

urlpatterns = [
    path('', HOME, name='home'),
    path('account/login/', LOGIN, name='login'),
    path('logout', LOGOUT, name='logout'),
    path('account/registration/', CU_REGISTRATION, name='cu_registration'),

    #! Admin and Editor -> Registration path
    path('account/admin/registration/', AD_REGISTRATION, name='ad_registration'),
    path('account/editor/registration/', ED_REGISTRATION, name='ed_registration'),

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)