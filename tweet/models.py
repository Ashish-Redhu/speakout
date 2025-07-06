from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Link to the User model, which is default in Django
    content = models.TextField(max_length=240) # Content of the tweet, limited to 240 characters
    photo = models.ImageField(upload_to='photos/', blank=True, null=True) # Optional photo upload for the tweet
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}..."  # Display first 20 characters of the tweet content
