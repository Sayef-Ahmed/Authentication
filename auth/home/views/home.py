from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from account.decorators import allowed_users


# @login_required
# @allowed_users(allowed_roles=['customer'])
def HOME(request):

    return render(request, 'customer/main/home.html')

#! ==========================================================

def LOGIN(request):

    pass
    # return render(request, 'accounts/login_registration/login.html')

#! ==========================================================

def LOGOUT(request):

    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('home')

#! ==========================================================

def CU_REGISTRATION(request):

    return render(request, 'accounts/login_registration/customer_registration.html')


#! ==========================================================
#? Admin and Editor Registration

def AD_REGISTRATION(request):

    return render(request, 'accounts/login_registration/admin_registration.html')   


def ED_REGISTRATION(request):

    return render(request, 'accounts/login_registration/editor_registration.html')



