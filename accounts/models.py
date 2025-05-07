from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.db import models
from django.utils import timezone
from datetime import timedelta
import re

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
        extra_fields.setdefault('is-staff',True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'superuser')
        return self.create_user(phone, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('student', 'دانشجو'),
        ('teacher', 'مدرس'),
        ('support', 'پشتیبانی'),
        ('financial', 'مالی'),
        ('content', 'محتوا'),
        ('superuser', 'سوپریوزر'),
    )
    phone = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    data_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone
        
class UserProfile(models.Model):
    user = models.OneToOneField('AUTH_USER_MODEL', on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    national_code = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], blank=True)
    birth_date = models.DateField(null=True, blank=True)
    