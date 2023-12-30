import os

from loguru import logger

__all__ = ['logger']

## configure logger for save logs in logs folder
path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'events.log')
if not os.path.exists(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

format_pattern = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {message} | {exception} | {extra}"
logger.add(path, enqueue=True, retention="7 days", format=format_pattern, rotation="100 MB", compression="zip")
