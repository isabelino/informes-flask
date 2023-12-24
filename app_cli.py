from api_v2.conexion import repo_session, repo
from api_v2.models import ModelBase


class AppCli:
    def __init__(self, app=None):
        if not app is None:
            self.init_app(app)

    def init_app(self, app):
        @app.cli.command()
        def initdb():
            """
            Crear la base de datos
            :return:
            """
            with repo() as db:
                ModelBase.metadata.create_all(db.get_engine())

        @app.cli.command()
        def dropdb():
            """
            Borrar la base de datos
            :return:
            """
            with repo() as db:
                ModelBase.metadata.drop_all(db.get_engine())
