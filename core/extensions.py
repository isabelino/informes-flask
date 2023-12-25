from typing import Protocol


class ScriptObject(Protocol):

    def __init__(self):
        self.result = None

    def script(self) -> str:
        ...

    def execute(self, db, **params):
        self.result = db.execute(self.script(), **params)

    def fetch_all(self):
        return self.result.fetchall()

    def fetch_one(self):
        return self.result.fetchone()

    def fetch_scalar(self):
        return self.result.scalar()
