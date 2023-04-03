from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Record(models.Model):
    name = models.CharField(max_length=255, default="default_name")
    illness = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField("CustomUser", related_name="record_users")

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
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


class UserRecord(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_records"
    )
    record = models.ForeignKey(
        Record, on_delete=models.CASCADE, related_name="user_records_created"
    )

    class Meta:
        unique_together = ["user", "record"]
