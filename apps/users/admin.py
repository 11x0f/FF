from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("alias", "email", "phone", "is_staff", "created_at")
    list_filter = ("is_staff", "is_active")
    search_fields = ("alias", "email")
    ordering = ("-created_at",)

    fieldsets = (
        (None, {"fields": ("email", "alias", "password")}),
        ("Profile", {"fields": ("phone", "avatar", "bio")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "alias", "password1", "password2"),
        }),
    )