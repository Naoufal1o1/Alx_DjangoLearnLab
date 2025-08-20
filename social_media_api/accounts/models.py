from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

def upload_to(instance, filename):
    return f"profiles/{instance.username}/{filename}"

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to=upload_to, blank=True, null=True)
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",
        blank=True,
    )

    def __str__(self):
        return self.username
