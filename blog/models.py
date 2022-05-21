from django.db import models
from django.contrib.auth.models import User

class Blogs(models.Model):
    original_heading = models.CharField(max_length=255)
    blog_heading = models.CharField(max_length=255,blank=True)
    blog_content=models.TextField()
    blog_image=models.CharField(max_length=255)
    publish_date=models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    content_source = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    class Meta:
        ordering = ['-created_on']

        def __unicode__(self):
            return self.blog_heading
    