from django.contrib import admin
from . import models


@admin.register(models.Task)
class NotesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'created_at'
    )
