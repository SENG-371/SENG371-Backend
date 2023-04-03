from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password


class Record(models.Model):
    name = models.CharField(max_length=255, default="default_name")
    illness = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField("Patients", related_name="record_users")

    def __str__(self):
        return self.name


class Patients(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    riskLevel = models.CharField(max_length=255, blank=True, null=True)
    records = models.ManyToManyField(Record, related_name="user_records")

    groups = models.ManyToManyField(
        "auth.Group",
        blank=True,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        blank=True,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    username = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.username


class PatientRecord(models.Model):
    user = models.ForeignKey(
        Patients, on_delete=models.CASCADE, related_name="user_records"
    )
    record = models.ForeignKey(
        Record, on_delete=models.CASCADE, related_name="user_records_created"
    )

    class Meta:
        unique_together = ["user", "record"]


class Practitioner(AbstractUser):
    practitioner_id = models.CharField(max_length=150, unique=True)
    patients = models.ManyToManyField(Patients, related_name="practitioner_patients")

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="practitioners",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="practitioners",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        default="default_username",
    )

    password = models.CharField(
        _("password"),
        max_length=128,
        help_text=_("Required. Must be set."),
        default=make_password("default_password"),
    )

    def __str__(self):
        return self.practitioner_id
