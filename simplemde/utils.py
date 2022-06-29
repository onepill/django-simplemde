from django.core.exceptions import ImproperlyConfigured
from importlib import import_module

try:
    # django > 3 
    from django.utils.encoding import force_str
except ImportError:
    # django 2 
    from django.utils.encoding import force_unicode as force_str

from django.utils.functional import Promise

import json


class LazyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Promise):
            return force_str(obj)
        return super(LazyEncoder, self).default(obj)


def json_dumps(data):
    return json.dumps(data, cls=LazyEncoder)
