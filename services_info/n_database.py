

class Database:

    def __init__(self, **kwargs):
        """Inicializa la base de datos"""
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.database = kwargs.get('database') or ''
        self.host = kwargs.get('host')
        self.port = kwargs.get('port') or '3306'
        self.echo = kwargs.get('echo') or False
        self.driver = 'mysql+pymysql'
        self.charset = 'utf8'
        self.url = f"{self.driver}://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        self.engine = create_engine(self.url, poolclass=NullPool)
        self.cn = self.engine.connect()
        self.metadata = MetaData()

    def select_database(self, db: str)->None:
        """Selecciona la base de datos"""
        self.database = db
        self.execute(f'use {db.strip().lower()}')

    def execute(self, query: str, **kwargs):
        """Ejecuta una consulta y devuelve un cursor"""
        # done: validar que la consulta no sea una consulta de selección
        return self.cn.execute(text(query), **kwargs)

    def fetch_all(self, query: str, **kwargs):
        """Devuelve una lista de tuplas"""
        return self.execute(query, **kwargs).fetchall()

    def fetch_one(self, query: str, **kwargs):
        """Devuelve una tupla"""
        return self.execute(query, **kwargs).fetchone()

    def fetch_scalar(self, query: str, **kwargs):
        """Devuelve un valor escalar"""
        return self.execute(query, **kwargs).scalar()

    def get_engine(self):
        """Devuelve el motor de base de datos"""
        return self.engine

    def get_metadata(self):
        """Devuelve el metadata de la base de datos"""
        return self.metadata

    def get_cursor(self, query: str, **kwargs):
        """Devuelve un cursor"""
        return self.cn.execute(text(query), **kwargs).cursor

    def get_session(self):
        """Devuelve una sesión de la base de datos"""
        return sessionmaker(bind=self.engine)()

    def table_exists(self, table_cls):
        """Devuelve True si la tabla existe"""
        instance = table_cls()
        tablename = instance.__tablename__

        if self.driver.startswith("mysql"):
            # mysql
            query = f"select count(*) from information_schema.tables where table_schema = '{self.database}' and table_name = '{tablename}'"
        else:
            # sqlite
            query = f"select count(*) from sqlite_master where type = 'table' and name = '{tablename}'"

        return self.execute(query).scalar() > 0

    def create_table(self, table_cls):
        """Crea una tabla en la base de datos"""
        table_cls().__table__.create(bind=self.engine, checkfirst=True)
        self.__execute_setup(table_cls)

    def __execute_setup(self, classname):
        """
        Ejecuta el setup de una clase
        :param classname:
        :return:
        """
        instance = classname()
        if hasattr(instance, 'setup'):
            list_instance = instance.setup()
            for item in list_instance:
                s = self.get_session()
                s.merge(item) if item.codigo is not None else s.add(item)
                s.commit()

        if hasattr(instance, 'triggers'):
            print(f"found triggers in class  {classname.__tablename__}")
            list_instance = instance.triggers()
            for item in list_instance:
                print("executing trigger", item.build())
                self.execute(item.build())


@contextlib.contextmanager
def repo():
    """Devuelve una sesión de la base de datos"""
    d = Database(username=os.getenv('DATABASE_USER'),
                 password=os.getenv('DATABASE_PASS'),
                 host=os.getenv('DATABASE_HOST'),
                 port=os.getenv('DATABASE_PORT'),
                 database=os.getenv('DATABASE_NAME'),
                 debug=os.getenv('DATABASE_DEBUG'),
                 echo=os.getenv('DATABASE_ECHO'))
    # d.select_database('dr2gsistemas_market')
    yield d
    d.cn.close()

