from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'پروفایل'
    fk_name = 'user'

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = [UserProfileInline]
    model = User
    list_display = ['phone', 'role', 'is_staff', 'is_active']
    list_filter = ['role', 'is_staff', 'is_active']
    search_fields = ['phone']
    ordering = ['-date_joined']
    
    #ask how this works 
    # fieldsets = (
 
    # )

    # add_fieldsets = (

    # )

    def get_inline_instances(self, request, obj = None):
        if not obj:
            return[]
        return super().get_inline_instances(request, obj)