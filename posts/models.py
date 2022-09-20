
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'post'
    
    name = models.CharField(
        'Name', blank=False, null=False, max_length=50, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'Body', blank=False, null=False, max_length=500, db_index=True, default='What\'s Happening?'
    )
    created_at = models.DateTimeField(
     'Created DateTime', blank=True, auto_now_add=True   
    )
    updated_at = models.DateTimeField(
     'Updated DateTime', blank=True, auto_now=True   
    )
    image = CloudinaryField(
        'image', blank = True
    )
    likes = models.PositiveBigIntegerField('like', default=0, blank = True)

    def __str__(self):
        return self.name