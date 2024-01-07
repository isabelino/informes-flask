from sqlalchemy import *
from sqlalchemy.orm import *

__all__ = ['ModelBase', 'ModelContadores', 'ModelFC03', 'ModelFC04', 'ModelFC05', 'ModelFC06', 'ModelFC10',
           'ModelMovement']


class ModelBaseClass:
    __table_args__ = {
        'extend_existing': True,
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_unicode_ci'
    }
    __version__ = '1.0'
    id = Column(INTEGER, primary_key=True, autoincrement=True, comment='Codigo del registro')

    def as_dict(self) -> dict:
        """
        Transforma el objeto en un diccionario
        :return:
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def from_dict(self, data):
        """
        Transforma un diccionario en el objeto
        :param data:
        :return:
        """
        for key, value in data.items():
            if key in self.__table__.columns:
                setattr(self, key, value)


ModelBase = declarative_base(cls=ModelBaseClass)


class ModelContadores(ModelBase):
    __tablename__ = 'contadores'
    # __table_args__.update({'comment': 'Contadores de los registros de la base de datos'})
    informe = Column(VARCHAR(50), nullable=False, comment='Nombre del informe')
    numero = Column(INTEGER, nullable=False, comment='Numero del informe')
    fecha = Column(DATE, nullable=False, comment='Fecha del informe')


class ModelFC03(ModelBase):
    __tablename__ = 'informe_fc03'
    # __table_args__.update({'comment': 'Informe de la FC03'})
    entidad = Column(VARCHAR(150), nullable=True, comment='Entidad')
    unidad_jerarquica = Column(VARCHAR(150), nullable=True, comment='Unidad jerarquica')
    reparticion = Column(VARCHAR(150), nullable=True, comment='Reparticion')
    dependencia = Column(VARCHAR(150), nullable=True, comment='Dependencia')
    area = Column(VARCHAR(150), nullable=True, comment='Area')
    origen = Column(VARCHAR(150), nullable=True, comment='Origen')
    cuenta = Column(VARCHAR(150), nullable=True, comment='Cuenta')
    sub_cuenta = Column(VARCHAR(150), nullable=True, comment='Sub cuenta')
    analitico_1 = Column(VARCHAR(150), nullable=True, comment='Analitico 1')
    analitico_2 = Column(VARCHAR(150), nullable=True, comment='Analitico 2')
    descripcion = Column(VARCHAR(150), nullable=True, comment='Descripcion')
    fecha = Column(DATE, nullable=True, comment='Fecha')
    tipo = Column(VARCHAR(150), nullable=True, comment='Tipo')
    numero = Column(VARCHAR(150), nullable=True, comment='Numero')
    rotulado = Column(VARCHAR(150), nullable=True, comment='Rotulado')
    cantidad = Column(DECIMAL(10, 2), nullable=True, comment='Cantidad')
    valor_unitario = Column(DECIMAL(10, 2), nullable=True, comment='Valor unitario')
    valor_total = Column(DECIMAL(10, 2), nullable=True, comment='Valor total')
    signo = Column(VARCHAR(150), nullable=True, comment='Signo')
    fecha_incorp = Column(DATE, nullable=True, comment='Fecha de incorporacion')
    vida_util = Column(INTEGER, nullable=True, comment='Vida util')
    origen_movi = Column(VARCHAR(150), nullable=True, comment='Origen del movimiento')
    sub_total = Column(DECIMAL(10, 2), nullable=True, comment='Sub total')
    iva = Column(DECIMAL(10, 2), nullable=True, comment='IVA')
    totales = Column(DECIMAL(10, 2), nullable=True, comment='Totales')
    numero_informe = Column(INTEGER, nullable=True, comment='Numero del informe')
    fecha_informe = Column(DATE, nullable=True, comment='Fecha del informe')
    item = Column(JSON(True), nullable=True, comment='Items')
    reparticion_cod = Column(VARCHAR(150), nullable=True, comment='Codigo de la reparticion')
    dependencia_cod = Column(VARCHAR(150), nullable=True, comment='Codigo de la dependencia')
    cont_informe = Column(INTEGER, nullable=True, comment='Contador del informe')


class ModelFC04(ModelBase):
    __tablename__ = 'informe_fc04'
    __table_args__ = {'comment': 'Informe de la FC04'}
    unidad_jerarquica = Column(VARCHAR(150), nullable=True, comment='Unidad jerarquica')
    entidad = Column(VARCHAR(150), nullable=True, comment='Entidad')
    entidad_text = Column(VARCHAR(150), nullable=True, comment='Entidad')
    reparticion = Column(VARCHAR(150), nullable=True, comment='Reparticion')
    reparticion_text = Column(VARCHAR(150), nullable=True, comment='Reparticion')
    dependencia = Column(VARCHAR(150), nullable=True, comment='Dependencia')
    origen_movimiento = Column(VARCHAR(150), nullable=True, comment='Origen del movimiento')
    items = Column(JSON(True), nullable=True, comment='Items')
    nro_informe = Column(VARCHAR(150), nullable=True, comment='Numero del informe')
    fecha_informe = Column(VARCHAR(50), nullable=True, comment='Fecha del informe')
    observacion = Column(VARCHAR(10000), nullable=True, comment='Observacion')
    cont_informe = Column(INTEGER, nullable=True, comment='Contador del informe')
    sub_total = Column(VARCHAR(50), nullable=True, comment='Sub total')
    iva = Column(VARCHAR(150), nullable=True, comment='IVA')
    totales = Column(VARCHAR(150), nullable=True, comment='Totales')
    cuenta = Column(VARCHAR(150), nullable=True, comment='Cuenta')


class ModelFC05(ModelBase):
    __tablename__ = 'informe_fc05'
    __table_args__ = {'comment': 'Informe de la FC05'}
    fecha = Column(VARCHAR(50), nullable=True, comment='Fecha')
    cuenta = Column(VARCHAR(150), nullable=True, comment='Cuenta')
    nombre_cuenta = Column(VARCHAR(150), nullable=True, comment='Nombre de la cuenta')
    valor_unitario = Column(DECIMAL(10, 2), nullable=True, comment='Valor unitario')
    origen = Column(VARCHAR(150), nullable=True, comment='Origen')
    saldo = Column(DECIMAL(10, 2), nullable=True, comment='Saldo')
    total = Column(DECIMAL(10, 2), nullable=True, comment='Total')
    numero_informe = Column(INTEGER, nullable=True, comment='Numero del informe')
    fecha_informe = Column(VARCHAR(50), nullable=True, comment='Fecha del informe')
    month = Column(VARCHAR(10), nullable=True, comment='Mes')
    year = Column(VARCHAR(10), nullable=True, comment='Año')

    @validates("nombre_cuenta")
    def validates_nombre_cuenta(self, key, value):
        if isinstance(value, str):
            value = value.upper()
        return value.replace('  ', ' ')


class ModelFC06(ModelBase):
    __tablename__ = 'informe_fc06'
    # __table_args__.update({'comment': 'Informe de la FC06'})

    cuenta = Column(VARCHAR(150), nullable=False, comment='Cuenta')
    sub_cuenta = Column(VARCHAR(150), nullable=False, comment='Sub cuenta')
    nombre_cuenta = Column(VARCHAR(150), nullable=False, comment='Nombre de la cuenta')
    analitico = Column(VARCHAR(150), nullable=False, comment='Analitico')
    cantidad = Column(DECIMAL(10, 2), nullable=False, comment='Cantidad')
    valor_parcial = Column(DECIMAL(10, 2), nullable=False, comment='Valor parcial')
    valor_total = Column(DECIMAL(10, 2), nullable=False, comment='Valor total')
    unidad_jerarquica = Column(VARCHAR(150), nullable=False, comment='Unidad jerarquica')
    reparticion = Column(VARCHAR(150), nullable=False, comment='Reparticion')
    dependencia = Column(VARCHAR(150), nullable=False, comment='Dependencia')
    numero_informe = Column(INTEGER, nullable=False, comment='Numero del informe')
    fecha_informe = Column(DATE, nullable=False, comment='Fecha del informe')
    month = Column(INTEGER, nullable=False, comment='Mes')
    year = Column(INTEGER, nullable=False, comment='Año')


class ModelFC10(ModelBase):
    __tablename__ = 'informe_fc10'
    # __table_args__.update({'comment': 'Informe de la FC10'})
    entidad = Column(VARCHAR(150), nullable=True, comment='Entidad')
    entidad_text = Column(VARCHAR(150), nullable=True, comment='Entidad')
    unidad_jerarquica = Column(VARCHAR(150), nullable=True, comment='Unidad jerarquica')
    reparticion = Column(VARCHAR(150), nullable=True, comment='Reparticion')
    reparticion_text = Column(VARCHAR(150), nullable=True, comment='Reparticion')
    dependencia = Column(VARCHAR(150), nullable=True, comment='Dependencia')
    dependencia_text = Column(VARCHAR(150), nullable=True, comment='Dependencia')
    responsable = Column(VARCHAR(150), nullable=True, comment='Responsable')
    cargo = Column(VARCHAR(150), nullable=True, comment='Cargo')
    items = Column(JSON(True), nullable=True, comment='Items')
    fecha_informe = Column(VARCHAR(50), nullable=True, comment='Fecha del informe')
    numero_informe = Column(VARCHAR(150), nullable=True, comment='Numero del informe')
    cont_informe = Column(INTEGER, nullable=True, comment='Contador del informe')
    cuenta = Column(VARCHAR(150), nullable=True, comment='Cuenta')
    total = Column(VARCHAR(150), nullable=True, comment='Total')


class ModelMovement(ModelBase):
    __tablename__ = 'movements'
    __table_args__ = {'comment': 'Movimientos'}
    date = Column(DATE, nullable=False, comment='Fecha')
    concept = Column(VARCHAR(150), nullable=False, comment='Concepto')
    quantity = Column(DECIMAL(10, 2), nullable=False, comment='Cantidad')
