from django.db import models


class Record(models.Model):
    illness = models.CharField(max_length=30)
    description = models.TextField(max_length=100)

    def __str__(self) -> str:
        return self.illness
