### api informes

Información importante

- Python 3.10 y Flask 2.2
- Crear un entorno virual y agregar los modulos necesarios en el requirements.txt
- utiliza base de datos sqlite

## Comando para administrar base de datos

- Para inicializar la base de datos

````bash
$ set FLASK_APP=main.py
$ flask initdb
````

- Para borrar la base de datos

````bash
$ flask dropdb

````

- Parametros de base de datos

````dotenv
# database settings for prod
DATABASE_HOST=db
DATABASE_PORT=3306
DATABASE_NAME=senave_database
DATABASE_USER=root
DATABASE_PASS=root
````