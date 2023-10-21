import uuid as uuid
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True)

    is_done = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Done's status"
    )

    title = models.CharField(
        max_length=155,
        null=False,
        blank=False,
        verbose_name="Title"
    )

    desc = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Desc"
    )

    user = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name="User"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
