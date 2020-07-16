from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=255)
    text = RichTextUploadingField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title