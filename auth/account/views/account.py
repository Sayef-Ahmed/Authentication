from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib import messages
from account.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login
from account.decorators import unauthenticated_user
from account.models import *
import re


@unauthenticated_user
def LOGIN(request):

    if request.method == 'POST':
        email = request.POST.get('email', '').lower().strip()
        password = request.POST.get('password', '')

        #? user to email chanege (user ke email dara poriborton kora hoise)
        # --- start ---
        user = EmailBackEnd().authenticate(request, 
        username=email,
        password=password)

        #! All login
        if user is not None:
            login(request, user)

            if request.GET.get('next',None):
                return HttpResponseRedirect(request.GET['next'])

            type_obj = UserType.objects.get(user=user)
            if user.is_authenticated and type_obj.is_admin:
                return redirect('admin_dashbord:dashbord') #Go to Admin home
            elif user.is_authenticated and type_obj.is_customer:
                return redirect('home') #Go to Customer home
            elif user.is_authenticated and type_obj.is_editor:
                return redirect('editor:dashbord') #Go to Editor home

        else:
            # Invalid email or password. Handle as you wish
            messages.error(request, 'Email and Password Are Invalid !')
            return redirect('login')

    return render(request, 'accounts/login_registration/login.html')

#! ==========================================================

#! Customer Registration
@unauthenticated_user
def CUSTOMER_REGISTRATION(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cu = request.POST.get('customer')

        # Chek Email
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email are Already Exists !')
            return redirect('cu_registration')

        # Check Username
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username are Already Exists !')
            return redirect('cu_registration')

        if len(password)<5 :
            messages.warning(request,"Password must be at last 6 characters long.")
            return redirect('cu_registration')

        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        #? Advance Security
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        if not re.search (r"[A-Z]", password) :
            messages.warning(request,"Password must contain at least one uppercase letter.")
            return redirect('cu_registration')

        if not re.search (r"[a-z]", password) :
            messages.warning(request,"Password must contain at least one lowercase letter.")
            return redirect('cu_registration')

        if not re.search (r"[0-9]", password) :
            messages.warning(request,"Password must contain at least one number.")
            return redirect('cu_registration')

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            messages.warning(request,"Password must contain at last one special character.")
            return redirect('cu_registration')
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        
        user = CustomUser(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        #! Save one by one
        usero = None
        if cu:
            usero = CUSTOMER(user=user)

        usero.save()

        # #! Save All
        usert = None
        if cu:
            usert = UserType(user=user,is_customer=True)
        
        usert.save()

        #Successfully registered. Redirect to Loginpage
        return redirect('login')

    return render(request, 'accounts/login_registration/customer_registration.html')

#! ==========================================================

#! Multiple Registration
def MULTIPLE_REGISTRATION(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        ad = request.POST.get('admin')
        cu = request.POST.get('customer')
        ed = request.POST.get('editor')

        # Chek Email
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email are Already Exists !')
            return redirect('customer-registration')

        # Check Username
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username are Already Exists !')
            return redirect('customer-registration')

        if len(password)<5 :
            messages.warning(request,"Password must be at last 6 characters long.")
            return redirect('cu_registration')

        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        #? Advance Security
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        if not re.search (r"[A-Z]", password) :
            messages.warning(request,"Password must contain at least one uppercase letter.")
            return redirect('cu_registration')

        if not re.search (r"[a-z]", password) :
            messages.warning(request,"Password must contain at least one lowercase letter.")
            return redirect('cu_registration')

        if not re.search (r"[0-9]", password) :
            messages.warning(request,"Password must contain at least one number.")
            return redirect('cu_registration')

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            messages.warning(request,"Password must contain at last one special character.")
            return redirect('cu_registration')
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        user = CustomUser(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        #! Save one by one
        usero = None
        if ad:
            usero = ADMIN(user=user)
        elif cu:
            usero = CUSTOMER(user=user)
        elif ed:
            usero = EDITOR(user=user)

        usero.save()

        # #! Save All
        usert = None
        if ad:
            usert = UserType(user=user,is_admin=True)
        elif cu:
            usert = UserType(user=user,is_customer=True)
        elif ed:
            usert = UserType(user=user,is_editor=True)
        
        usert.save()

        #Successfully registered. Redirect to Admin Setting Page
        return redirect('login')

    return render(request, 'accounts/login_registration/admin_registration.html')

#! ==========================================================

#! Admin Registration
def ADMIN_REGISTRATION(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        ad = request.POST.get('admin')

        # Chek Email
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email are Already Exists !')
            return redirect('customer-registration')

        # Check Username
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username are Already Exists !')
            return redirect('customer-registration')

        if len(password)<5 :
            messages.warning(request,"Password must be at last 6 characters long.")
            return redirect('cu_registration')

        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        #? Advance Security
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        if not re.search (r"[A-Z]", password) :
            messages.warning(request,"Password must contain at least one uppercase letter.")
            return redirect('cu_registration')

        if not re.search (r"[a-z]", password) :
            messages.warning(request,"Password must contain at least one lowercase letter.")
            return redirect('cu_registration')

        if not re.search (r"[0-9]", password) :
            messages.warning(request,"Password must contain at least one number.")
            return redirect('cu_registration')

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            messages.warning(request,"Password must contain at last one special character.")
            return redirect('cu_registration')
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        user = CustomUser(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        #! Save one by one
        usero = None
        if ad:
            usero = ADMIN(user=user)

        usero.save()

        # #! Save All
        usert = None
        if ad:
            usert = UserType(user=user,is_admin=True)
        
        usert.save()

        #Successfully registered. Redirect to Admin Setting Page
        return redirect('login')

    return render(request, 'accounts/login_registration/admin_registration.html')

#! ==========================================================

#! Editor Registration
def EDITOR_REGISTRATION(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        ed = request.POST.get('editor')

        # Chek Email
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email are Already Exists !')
            return redirect('customer-registration')

        # Check Username
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username are Already Exists !')
            return redirect('customer-registration')

        if len(password)<5 :
            messages.warning(request,"Password must be at last 6 characters long.")
            return redirect('cu_registration')

        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        #? Advance Security
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        if not re.search (r"[A-Z]", password) :
            messages.warning(request,"Password must contain at least one uppercase letter.")
            return redirect('cu_registration')

        if not re.search (r"[a-z]", password) :
            messages.warning(request,"Password must contain at least one lowercase letter.")
            return redirect('cu_registration')

        if not re.search (r"[0-9]", password) :
            messages.warning(request,"Password must contain at least one number.")
            return redirect('cu_registration')

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            messages.warning(request,"Password must contain at last one special character.")
            return redirect('cu_registration')
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        user = CustomUser(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        #! Save one by one
        usero = None
        if ed:
            usero = EDITOR(user=user)

        usero.save()

        # #! Save All
        usert = None
        if ed:
            usert = UserType(user=user,is_editor=True)
        
        usert.save()

        #Successfully registered. Redirect to Admin Setting Page
        return redirect('ed_registration')

    return render(request, 'accounts/login_registration/editor_registration.html')

#! ==========================================================


