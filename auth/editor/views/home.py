from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from account.decorators import allowed_users
from django.contrib import messages
from django.contrib.auth import logout


@login_required
@allowed_users(allowed_roles=['editor'])
def Editor(request):

    return render(request, 'editor/main/home.html')

#! ==========================================================

def LOGIN(request):

    return render(request, 'accounts/login_registration/login.html')

#! ==========================================================

def LOGOUT(request):

    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('home')

    return HttpResponse('home')

#! ==========================================================

def ED_REGISTRATION(request):

    return render(request, 'accounts/login_registration/editor_registration.html')
