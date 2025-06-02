from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),

    #! Accounts
    path('account/', include('account.urls')),
    path('admin_dashbord/accounts/', include('account.urls')),
    path('editor/accounts/', include('account.urls')),

    #! All Dashboards
    path('admin_dashbord/', include('admin_dashbord.urls', namespace='admin_dashbord')),
    path('editor/', include('editor.urls', namespace='editor')),

    #! Home
    path('', include('home.urls')),

]