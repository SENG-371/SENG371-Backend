from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Patients, Record, PatientRecord, Practitioner


class PatientsAdmin(UserAdmin):
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


class PractitionerAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "practitioner_id",
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
                    "practitioner_id",
                    "patients",
                )
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    filter_horizontal = ("patients", "user_permissions", "groups")

    search_fields = ("username", "email", "first_name", "last_name")


admin.site.register(Patients, PatientsAdmin)
admin.site.register(Practitioner, PractitionerAdmin)
admin.site.register(Record)
admin.site.register(PatientRecord)
