from django.db import models
from simplemde.fields import SimpleMDEField

# Create your models here.
class Markdown(models.Model):
    title = models.CharField(max_length=32)
    content = SimpleMDEField()
