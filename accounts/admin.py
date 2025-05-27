from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile

from django.utils.translation import gettext_lazy as _

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'پروفایل'
    fk_name = 'user'


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "phone",
    )
    search_fields = ("phone", "first_name", "last_name", "email")
    ordering = ("phone",)
    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
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
                "fields": ("phone", "usable_password", "password1", "password2"),
            },
        ),
    )
