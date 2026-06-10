from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Contact


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("id", "full_name", "title", "phone", "linkedin", "github")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal info", {"fields": ("full_name", "title", "bio", "phone", "location", "avatar", "cv")}),
        ("Social links", {"fields": ("linkedin", "github", "gmail", "telegram", "instagram", "youtube")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "full_name", "password1", "password2"),
        }),
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_read")
    list_filter = ("is_read",)
    readonly_fields = ("created_at",)
    actions = ["mark_as_read"]

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected as read"
