from django.contrib import admin

# Register your models here.
from .models import Blogs
from django_summernote.admin import SummernoteModelAdmin


class BlogsAdmin(SummernoteModelAdmin):
    list_display = ['blog_heading']

admin.site.register(Blogs,BlogsAdmin)