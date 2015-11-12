# django-simplemde
Use markdown editor https://github.com/NextStepWebs/simplemde-markdown-editor in django project, this project is inspired by https://github.com/douglasmiranda/django-wysiwyg-redactor/ 

# Getting started
* install django-simplemde
```
pip install django-simplemde
```

* add 'simplemde' to INSTALLED_APPS.
```python
INSTALLED_APPS = (
    # ...
    'simplemde',
    # ...
)
```

# Using in models
```python
from django.db import models
from simplemde.fields import SimpleMDEField

class Entry(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    content = SimpleMDEField(verbose_name=u'mardown content')
```

