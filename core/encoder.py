import datetime
import decimal
import json
from builtins import issubclass

from api_v2.models import ModelBase


class CustomJsonEncoder(json.JSONEncoder):

    def default(self, obj):

        if isinstance(obj, list):
            return [self.default(o) for o in obj]
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        elif issubclass(obj.__class__, ModelBase):
            return obj.as_dict()
        elif isinstance(obj, Exception):
            return repr(obj)

        return json.JSONEncoder.default(self, obj)
