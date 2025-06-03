from django.contrib import admin
from bootcamps.models import Bootcamp, BootcampRegistration, BootcampUser
from accounts.models import User
from bootcamps.tasks import send_approval_email, send_approval_sms

@admin.register(Bootcamp)
class BootcampAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'status', 'capacity', 'price']
    list_filter = ['status', 'start_date']
    search_fields = ['title']
    ordering = ['-start_date']

@admin.register(BootcampUser)
class BootcampUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'bootcamp', 'role', 'joined_at']
    list_filter = ['role']
    search_fields = ['user__phone']
    ordering = ['-joined_at']


@admin.register(BootcampRegistration)
class BootcampreguestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'bootcamp', 'role', 'status', 'created_at']
    list_filter = ['status', 'role']
    search_fields = ['full_name', 'phone']
    ordering = ['-created_at']
