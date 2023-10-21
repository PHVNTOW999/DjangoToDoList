import uuid as uuid
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        unique=True
    )

    is_done = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        verbose_name="Status"
    ),

    title = models.CharField(
        max_length=155,
        null=False,
        blank=False,
        verbose_name="Title"
    )

    desc = models.TextField(
        max_length=155,
        null=True,
        blank=True,
        verbose_name="Description"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="User"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        verbose_name="Created (Datetime)"
    )

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
