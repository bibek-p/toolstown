from django.contrib import admin

# Register your models here.
from .models import ToolsDetails
from django_summernote.admin import SummernoteModelAdmin


class ToolsDetailsAdmin(SummernoteModelAdmin):
    list_display = ['toolsname']

admin.site.register(ToolsDetails,ToolsDetailsAdmin)