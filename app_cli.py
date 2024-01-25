import os

import click
import tcppinglib

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

        @app.cli.command()
        def settings():
            click.secho('== SETTINGS ==', fg='green')
            click.echo(f"user: {os.getenv('DATABASE_USER')}")
            click.echo(f"pass: {os.getenv('DATABASE_PASS')}")
            click.echo(f"host: {os.getenv('DATABASE_HOST')}")
            click.echo(f"port: {os.getenv('DATABASE_PORT')}")
            click.echo(f"name: {os.getenv('DATABASE_NAME')}")
            click.secho('==============', fg='green')
            click.secho('== ENVIRONMENT ==', fg='green')
            for key, value in os.environ.items():
                click.echo(f"{key}: {value}")
            click.secho('================', fg='green')

        @app.cli.command()
        @click.argument('host', default='127.0.0.1', required=False)
        @click.argument('port', default=5000, required=False)
        def ping(host, port):
            click.secho(f'Pinging {host}:{port}...', fg='yellow')
            result = tcppinglib.tcpping(host, port)
            click.echo(result.is_alive)
