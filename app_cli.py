import os

import click

from api_v2.conexion import repo
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
            conexion_str = f"{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASS')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
            click.echo(f'Conectado con {conexion_str}')
            with repo() as db:
                ModelBase.metadata.create_all(db.get_engine())
            click.echo("Creada")

        @app.cli.command()
        def dropdb():
            """
            Borrar la base de datos
            :return:
            """
            conexion_str = f"{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASS')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
            click.echo(f'Conectado con {conexion_str}')
            with repo() as db:
                ModelBase.metadata.drop_all(db.get_engine())
            click.echo("Borrado")
