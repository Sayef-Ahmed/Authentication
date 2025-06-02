from django.db import models
from django.contrib.auth.models import AbstractUser

#! user model for the project
class CustomUser(AbstractUser):
    # is_admin = models.BooleanField(default=False)
    # is_customer = models.BooleanField(default=False)
    # is_editor = models.BooleanField(default=False)

    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('customer', 'Customer'),
    )

    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES, db_index=True)

    # # Personal Info
    # photo = models.ImageField(upload_to='custom_dashboard_photos/employ/', null=True, blank=True)
    # phone = models.CharField(max_length=20, null=True, db_index=True)

    # # Location Info
    # country = models.CharField(max_length=100, null=True, db_index=True)
    # city = models.CharField(max_length=100, null=True, db_index=True)
    # address = models.TextField(null=True)

    def __str__(self):
        return self.username
    
    def get_active_tasks(self):
        return self.assigned_tasks.filter(status__in=['todo', 'in_progress'])

#! Custom User Model
class UserType(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_customer= models.BooleanField(default=False)
    is_editor= models.BooleanField(default=False)

    def __str__(self):
        for field in self._meta.fields:
            if field.name.startswith('is_') and getattr(self, field.name):
                return f"{self.user.username} - {field.name}"
        return self.user.username
    
    #? Uncomment this method if you want to use a custom string representation
    # def __str__(self):
    #     if self.is_admin == True:
    #         return self.user.username + " - is_admin"
    #     elif self.is_customer == True:
    #         return self.user.username + " - is_customer"
    #     elif self.is_editor == True:
    #         return self.user.username + " - is_editor"

class ADMIN(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # address = models.CharField(max_length=500)
    # img = models.ImageField(default = "images/default.jpg", upload_to='Media/profile_images', null=True)


    def __str__(self):
        return self.user.username

class CUSTOMER(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # address = models.CharField(max_length=500)
    # img = models.ImageField(default = "images/default.jpg", upload_to='Media/profile_images', null=True)

    def __str__(self):
        return self.user.username

class EDITOR(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # address = models.CharField(max_length=500)
    # img = models.ImageField(default = "images/default.jpg", upload_to='Media/profile_images', null=True)

    def __str__(self):
        return self.user.username

