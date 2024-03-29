from django.db import models
from django.contrib.auth.models import User

class ToolsDetails(models.Model):
    toolsname = models.CharField(max_length=255)
    main_content = models.TextField(blank=True)
    page_titel=models.CharField(max_length=255)
    page_description=models.CharField(max_length=255)
    keyword=models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField(default="Tools Band")
    icon = models.ImageField(upload_to='images/icon')
    link = models.CharField(max_length=255)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.toolsname


