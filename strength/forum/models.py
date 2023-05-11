from django.db import models
from django.conf import settings
from django.urls import reverse
from login.models import Profile
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    name = models.CharField(max_length=100)
    context = models.TextField(max_length=1000)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    number = models.IntegerField(null=True)
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("forum:detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Comment(models.Model):
    context = models.TextField(max_length=1000)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", null=True)
    likes = models.ManyToManyField(User, related_name='likes')
    
    @property
    def total_likes(self):
        return self.likes.all().count()
        _
    def __str__(self):
        return "| " + str(self.author) + " | " + " - " + " | " + str(self.post) + " | "


LIKE_CHOICES = {
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),

}
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)