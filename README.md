# A markdown editor(with preview) for Django
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

# SimpleMDE options
You could set SimpleMDE options in settings.py like this:

```python
SIMPLEMDE_OPTIONS = {
    'placeholder': 'haha',
    'status': False,
    'autosave': {
        'enabled': True
    }
}
```

Right now this plugin supports [SimpleMDE Configurations](https://github.com/NextStepWebs/simplemde-markdown-editor#configuration), but only the static ones(don't support js configurations like ```previewRender```)

***for autosave option, you dont need to set it, this plugin will generate uniqueId with python's uuid.uuid4 automatically***

# Get SimpleMDE instance from DOM

After SimpleMDE initialized, you could get SimpleMDE instance from dom element like this:

```javascript
$('.simplemde-box')[0].SimpleMDE
```