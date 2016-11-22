from django.contrib import admin
from .models import Markdown
# Register your models here.
class MarkdownAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Markdown, MarkdownAdmin)