from django.core.exceptions import ImproperlyConfigured
from importlib import import_module

try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text
from django.utils.functional import Promise

import json


class LazyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)


def json_dumps(data):
    return json.dumps(data, cls=LazyEncoder)
