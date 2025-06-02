from django.contrib import admin
from .models import AdvCourse, AdvCourseUser, AdvCourseRegistration

@admin.register(AdvCourse)
class AdvCourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'capacity', 'is_live']
    list_filter = ['status', 'start_date']
    search_fields = ['title']
    ordering = ['-start_date']

@admin.register(AdvCourseUser)
class AdvCourseUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'advcourse', 'role', 'joined_at']
    list_filter = ['role']
    search_fields = ['user__phone']
    ordering = ['-joined_at']


@admin.register(AdvCourseRegistration)
class AdvCourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'advcourse', 'role', 'status', 'created_at']
    list_filter = ['status', 'role']
    search_fields = ['full_name', 'phone']
    ordering = ['-created_at']