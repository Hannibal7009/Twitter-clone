from django.db import models

# Create your models here.
from cloudinary.models import CloudinaryField


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )

    body = models.CharField(
        'Body', blank=True, null=True, max_length=140, db_index=True
    )

    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )

    like_count = models.PositiveBigIntegerField(
        'like', blank=True, null=True, default=0
    )

    image = CloudinaryField(
        'image', blank=True, null=True
    )
