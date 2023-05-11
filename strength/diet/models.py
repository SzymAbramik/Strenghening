from django.db import models
from django.conf import settings
from login.models import Profile
from django.urls import reverse


class Diet(models.Model):
    name = models.CharField(max_length=30)
    context = models.TextField(max_length=1000)
    image = models.ImageField(default="diet_pics/default.png", upload_to='diet_pics')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    cut_context = models.TextField(max_length=1000, null=True)


    def __str__(self):
        return str(self.id) + ' - ' + self.name

    def get_absolute_url(self):
        return reverse("diet:detail", args=[self.pk])

class Review(models.Model):
    context = models.TextField(max_length=1000)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=True)
    object = models.ForeignKey(Diet, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    number = models.IntegerField(null=True)
    def __str__(self):
        return str(self.object) + ' - ' + str(self.author)