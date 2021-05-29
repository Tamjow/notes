from django.db import models


class Note(models.Model):
    """A single note for storing information."""
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    expiration_date = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        ordering = ('title',)
