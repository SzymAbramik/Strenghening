from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(default="profile_pics/default.png", upload_to='profile_pics')
    description = models.TextField(max_length=1000, default="You didn't change your description yet!")
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("login:profile", args=[self.slug])
