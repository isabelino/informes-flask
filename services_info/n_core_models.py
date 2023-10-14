from sqlalchemy.orm import *
from sqlalchemy import *


__all__ = ['ModelBase']


class ModelBaseClass:
    __table_args__ = {
        'extend_existing': True,
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_unicode_ci'
    }
    __version__ = '1.0'
    id = Column(INTEGER, primary_key=True, autoincrement=True, comment='Codigo del registro')

    def as_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


ModelBase = declarative_base(cls=ModelBaseClass)


