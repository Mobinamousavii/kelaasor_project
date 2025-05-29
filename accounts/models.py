from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.db import models
from django.utils import timezone
from datetime import timedelta
import re
from django.conf import settings

class UserManager(BaseUserManager):
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
        extra_fields.setdefault('role', 'superuser')
        return self.create_user(phone, password, **extra_fields)
    

class Role(models.Model):
    group = models.CharField(max_length=100)

    def __str__(self):
        return self.group
    
class User(AbstractBaseUser, PermissionsMixin):


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
    
class OTPCode(models.Model):
    phone = models.CharField(max_length=15)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=2)
        super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return f"{self.phone_number} - {self.code}"
        
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    national_code = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], blank=True)
    birth_date = models.DateField(null=True, blank=True)
    

