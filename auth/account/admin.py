from django.contrib import admin
from .models import (CustomUser, UserType, ADMIN, CUSTOMER, EDITOR)


#! Register the main and proxy models
admin.site.register(CustomUser)
admin.site.register(UserType)
admin.site.register(ADMIN)
admin.site.register(CUSTOMER)
admin.site.register(EDITOR)

