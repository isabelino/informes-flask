from typing import Protocol

from sqlalchemy import CursorResult, TextClause

from api_v2.conexion import Database


class ScriptObject(Protocol):

    def __init__(self, db: Database):
        self.result = None
        self.db = db

    def script(self) -> TextClause:
        ...

    def __execute(self, **kwargs) -> CursorResult:
        return self.db.execute(self.script(), **kwargs)

    def fetch_all(self, **kwargs):
        return self.__execute(**kwargs).fetchall()

    def fetch_one(self, **kwargs):
        return self.__execute(**kwargs).fetchone()

    def fetch_scalar(self, **kwargs):
        return self.__execute(**kwargs).scalar()
