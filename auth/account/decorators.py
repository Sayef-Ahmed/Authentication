from django.shortcuts import redirect
from account.models import UserType

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                # Get or create the UserType for the logged-in user
                type_obj, created = UserType.objects.get_or_create(user=request.user)

                if type_obj.is_customer:
                    return redirect('home')
                elif type_obj.is_admin or request.user.is_superuser:
                    return redirect('admin_dashbord:dashbord')
                elif type_obj.is_editor:
                    return redirect('editor:dashbord')
                else:
                    return redirect('login')  # Fallback if no role is set

            except UserType.DoesNotExist:
                return redirect('login')  # Fallback if UserType doesn't exist
        return view_func(request, *args, **kwargs)  # Unauthenticated case
    return wrapper_func

def unauthenticated_dashboard(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                # Get or create the UserType for the logged-in user
                type_obj, created = UserType.objects.get_or_create(user=request.user)

                # Redirect based on user type
                if type_obj.is_admin or request.user.is_superuser:
                    return redirect('admin_dashbord:dashbord')
                elif type_obj.is_editor:
                    return redirect('editor:dashbord')
                else:
                    return redirect('login')  # Fallback if no role is set

            except UserType.DoesNotExist:
                return redirect('login')  # Fallback if UserType doesn't exist
        return view_func(request, *args, **kwargs)  # Unauthenticated case
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')

            try:
                # Get UserType object for the logged-in user
                type_obj = UserType.objects.get(user=request.user)

                # Map UserType to role
                if request.user.is_superuser:
                    group = 'admin'
                elif type_obj.is_admin:
                    group = 'admin'
                elif type_obj.is_editor:
                    group = 'editor'
                elif type_obj.is_customer:
                    group = 'customer'
                else:
                    group = None

                # Check if the group matches allowed roles
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    print(f"Access denied. User group: {group}, Required: {allowed_roles}")
                    return redirect('login')  # or a 403 page

            except UserType.DoesNotExist:
                print(f"UserType not found for: {request.user}")
                return redirect('login')  # Fallback if UserType doesn't exist

        return wrapper_func
    return decorator

