from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.home import Editor, LOGIN, LOGOUT, ED_REGISTRATION

app_name = 'editor'

urlpatterns = [
    path('', Editor, name='dashbord'),
    path('accounts/login/', LOGIN, name='login'),
    path('logout', LOGOUT, name='logout'),
    path('accounts/editor/registration/', ED_REGISTRATION, name='ed_registration'),

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)