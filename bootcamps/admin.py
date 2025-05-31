from django.contrib import admin
from .models import Bootcamp, BootcampRegistration, BootcampUser

@admin.register(Bootcamp)
class BootcampAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'status', 'capacity']
    list_filter = ['status', 'start_date']
    search_fields = ['title']
    ordering = ['-start_date']

@admin.register(BootcampRegistration)
class BootcampRequestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'bootcamp', 'role', 'status', 'created_at']
    list_filter = ['status', 'role']
    search_fields = ['full_name', 'phone']
    ordering = ['-created_at']

@admin.register(BootcampUser)
class BootcampUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'bootcamp', 'role', 'joined_at']
    list_filter = ['role']
    search_fields = ['user__phone']
    ordering = ['-joined_at']
