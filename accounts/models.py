from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.db import models
from django.utils import timezone
from datetime import timedelta
import re
from django.conf import settings

class UserManager(BaseUserManager):
    """
    Custom manager for User model that uses phone number instead of username.

    Methods:
        - create_user(phone, password, **extra_fields): Creates and returns a regular user.
        - create_superuser(phone, password, **extra_fields): Creates and returns a superuser.
        - normalize_phone(phone): Utility to clean up and normalize phone numbers.
    """
    def normalize_phone(self, phone):
        return re.sub(r'\D', '', phone)
    
    def create_user(self, phone, password =None, **extra_fields):
        if not phone:
            raise ValueError('phone number is required.')
        phone = self.normalize_phone(phone)
        user = self.model(phone = phone, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone, password = None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone, password, **extra_fields)
    

class Role(models.Model):
    """
    Represents a user role (e.g., student, support, admin).
    This model is used instead of traditional Django groups.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model using phone number as the unique identifier.

    Attributes:
        phone (str): Unique phone number of the user.
        full_name (str): User's full name (optional).
        is_active (bool): Determines whether this user should be treated as active.
        is_staff (bool): Determines whether the user can access the admin site.
        date_joined (datetime): The time the user joined.
        role (Role): The role assigned to the user (e.g., support, student).

    Methods:
        __str__: Returns the phone number.
        """

    phone = models.CharField(max_length=15, unique=True)
    full_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(to=Role,on_delete=models.SET_NULL, null=True, blank=True )

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone
    

        
class UserProfile(models.Model):
    """
    Extended profile for each user.

    Attributes:
        user (User): The related user.
        national_code (str): National identification number (optional).
        gender (str): Gender of the user ('male' or 'female').
        birth_date (date): User's date of birth.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    national_code = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], blank=True)
    birth_date = models.DateField(null=True, blank=True)
    

