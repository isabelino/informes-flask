import datetime
import decimal
import json
from builtins import issubclass

from api_v2.models import ModelBase
from api_v2.loggers import logger


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
        elif isinstance(obj, str) and (obj.startswith("[") or obj.startswith("{")):
            logger.debug(f'detected json: {obj}')
            return json.loads(obj)

        return json.JSONEncoder.default(self, obj)
