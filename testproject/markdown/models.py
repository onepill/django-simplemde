from django.db import models
from simplemde.fields import SimpleMDEField


class Markdown(models.Model):
    title = models.CharField(max_length=32)
    content = SimpleMDEField()
