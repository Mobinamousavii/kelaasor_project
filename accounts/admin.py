from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile, Role

from django.utils.translation import gettext_lazy as _

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'پروفایل'
    fk_name = 'user'


@admin.register(Role)
class Role(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "phone",
    )
    search_fields = ("phone",)
    ordering = ("phone",)
    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ("date_joined",)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('phone', 'password1', 'password2', 'role', 'is_staff', 'is_active'),
            },
        ),
    )
