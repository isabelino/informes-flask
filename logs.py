from loguru import logger
import os

__all__ = ['logger']
path = os.path.join(os.path.dirname(__file__), 'logs', 'events.log')
format_pattern = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
logger.add(path, enqueue=True, retention="1 days", format=format_pattern, rotation="100 MB", compression="zip")
