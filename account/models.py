from django.contrib.auth.models import AbstractUser
from django.db import models

from common.models import Media


class User(AbstractUser):
    full_name = models.CharField(max_length=150)
    title = models.CharField(max_length=100)        # e.g., "Fullstack Developer"
    bio = models.TextField()
    avatar = models.ForeignKey(
        Media, on_delete=models.SET_NULL, null=True, blank=True, related_name="user_avatars"
    )
    cv = models.FileField(upload_to="cv/", blank=True)
    phone = models.CharField(max_length=100)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    gmail = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    location = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        
        
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"
