from django.contrib.auth.models import AbstractUser
from django.db import models
from django.templatetags.static import static


def avatar_path(instance, filename):
    return f"avatars/{instance.id}/{filename}"


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=13, blank=True)
    avatar = models.FileField(default=None,
                              null=True,
                              blank=True,
                              upload_to=avatar_path)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url

        return static('anonymous-avatar.jpeg')
