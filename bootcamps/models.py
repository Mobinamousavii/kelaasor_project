from django.db import models
from django.conf import settings

class Bootcamp(models.Model):
    STATUS_CHOICES = (
        ('draft', 'پیش‌نویس'),
        ('registration_open', 'در حال ثبت‌نام'),
        ('in_progress', 'در حال برگزاری'),
        ('completed', 'برگزار شده'),
        ('canceled', 'لغو شده'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    days = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default= 'draft')

    def __str__(self):
        return self.title


class BootcampRegistrationRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'بررسی نشده'),
        ('reviewing', 'در حال بررسی'),
        ('approved', 'تایید شده'),
        ('rejected', 'تایید نشده'),
    )
    bootcamp = models.ForeignKey(Bootcamp, on_delete=models.CASCADE, related_name='requests')
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    national_code = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    role = models.CharField(max_length=10, choices=[('student', 'دانشجو'), ('mentor', 'منتور'), ('teacher', 'استاد')])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} - {self.bootcamp.title}'


class BootcampUser(models.Model):
    bootcamp = models.ForeignKey(Bootcamp, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('student', 'دانشجو'), ('mentor', 'منتور'), ('teacher', 'استاد')])
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('bootcamp', 'user')

    def __str__(self):
        return f'{self.user.phone} - {self.role} - {self.bootcamp.title}'