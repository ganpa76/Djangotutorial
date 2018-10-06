from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    userid = models.IntegerField(default=12)

    def __str__(self):
        return self.title