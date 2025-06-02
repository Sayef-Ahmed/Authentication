from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .views.account import *


urlpatterns = [

    #! Customer, Admin, Editor -> Login and Registration Page
    path('login/', LOGIN, name='login'),
    path('registration/', CUSTOMER_REGISTRATION, name='cu_registration'),

    #! Multiple -> Registration Page
    path('multiple-registration', MULTIPLE_REGISTRATION, name='multiple_registration'),

    #! Admin, Editor -> Registration Page
    path('admin/registration/', ADMIN_REGISTRATION, name='ad_registration'),
    path('editor/registration/', EDITOR_REGISTRATION, name='ed_registration'),


    # reset password urls #############################################
    path('password_reset/' , auth_views.PasswordResetView.as_view(template_name='accounts/forget_password/password_reset_form.html') , name='password_reset' ),
    path('password_reset/done/' , auth_views.PasswordResetDoneView.as_view(template_name='accounts/forget_password/password_reset_done.html') , name='password_reset_done' ),
    path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name='accounts/forget_password/password_reset_confirm.html') , name='password_reset_confirm' ),
    path('reset/done/' , auth_views.PasswordResetCompleteView.as_view(template_name='accounts/forget_password/password_reset_complete.html') , name='password_reset_complete' ),
    #################################################################### 

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
