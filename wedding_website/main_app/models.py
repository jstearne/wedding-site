from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from PIL import Image # pillow image manipulation
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=256, default='anonymous')
    rsvp = models.BooleanField(default=False)





class Post(models.Model):
    title: models.CharField(max_length=150)
    body: models.TextField(max_length=999)
    created_at = models.DateTimeField(auto_now_add=True)
    image = ImageField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
