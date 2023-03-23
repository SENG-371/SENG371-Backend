from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Record, UserRecord


class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "age",
        "birthday",
        "riskLevel",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            ("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "age",
                    "birthday",
                    "riskLevel",
                )
            },
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    filter_horizontal = (
        "groups",
        "user_permissions",
        "records",
    )
    search_fields = ("username", "email", "first_name", "last_name")


admin.site.register(User, CustomUserAdmin)


admin.site.register(Record)

admin.site.register(UserRecord)
