from sqlalchemy import Column, JSON

from sqlalchemy.orm import *
from sqlalchemy import *

__all__ = ['ModelBase','ModelContadores', 'ModelFC03', 'ModelFC04', 'ModelFC05', 'ModelFC06', 'ModelFC10']


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
    entidad = Column(VARCHAR(50), nullable=False, comment='Entidad')
    unidad_jerarquica = Column(VARCHAR(50), nullable=False, comment='Unidad jerarquica')
    reparticion = Column(VARCHAR(50), nullable=False, comment='Reparticion')
    dependencia = Column(VARCHAR(50), nullable=False, comment='Dependencia')
    area = Column(VARCHAR(50), nullable=False, comment='Area')
    origen = Column(VARCHAR(50), nullable=False, comment='Origen')
    cuenta = Column(VARCHAR(50), nullable=False, comment='Cuenta')
    sub_cuenta = Column(VARCHAR(50), nullable=False, comment='Sub cuenta')
    analitico_1 = Column(VARCHAR(50), nullable=False, comment='Analitico 1')
    analitico_2 = Column(VARCHAR(50), nullable=False, comment='Analitico 2')
    descripcion = Column(VARCHAR(50), nullable=False, comment='Descripcion')
    fecha = Column(DATE, nullable=False, comment='Fecha')
    tipo = Column(VARCHAR(50), nullable=False, comment='Tipo')
    numero = Column(VARCHAR(50), nullable=False, comment='Numero')
    rotulado = Column(VARCHAR(50), nullable=False, comment='Rotulado')
    cantidad = Column(DECIMAL(10, 2), nullable=False, comment='Cantidad')
    valor_unitario = Column(DECIMAL(10, 2), nullable=False, comment='Valor unitario')
    valor_total = Column(DECIMAL(10, 2), nullable=False, comment='Valor total')
    signo = Column(VARCHAR(50), nullable=False, comment='Signo')
    fecha_incorp = Column(DATE, nullable=False, comment='Fecha de incorporacion')
    vida_util = Column(INTEGER, nullable=False, comment='Vida util')
    origen_movi = Column(VARCHAR(50), nullable=False, comment='Origen del movimiento')
    sub_total = Column(DECIMAL(10, 2), nullable=False, comment='Sub total')
    iva = Column(DECIMAL(10, 2), nullable=False, comment='IVA')
    totales = Column(DECIMAL(10, 2), nullable=False, comment='Totales')
    numero_informe = Column(INTEGER, nullable=False, comment='Numero del informe')
    fecha_informe = Column(DATE, nullable=False, comment='Fecha del informe')
    item = Column(JSON(True), nullable=False, comment='Items')
    reparticion_cod = Column(VARCHAR(50), nullable=False, comment='Codigo de la reparticion')
    dependencia_cod = Column(VARCHAR(50), nullable=False, comment='Codigo de la dependencia')
    cont_informe = Column(INTEGER, nullable=False, comment='Contador del informe')


class ModelFC04(ModelBase):
    __tablename__ = 'informe_fc04'
    # __table_args__.update({'comment': 'Informe de la FC04'})
    unidad_jerarquica = Column(VARCHAR(50), nullable=False, comment='Unidad jerarquica')
    entidad = Column(VARCHAR(50), nullable=False, comment='Entidad')
    entidad_text = Column(VARCHAR(50), nullable=False, comment='Entidad')
    reparticion = Column(VARCHAR(50), nullable=False, comment='Reparticion')
    reparticion_text = Column(VARCHAR(50), nullable=False, comment='Reparticion')
    dependencia = Column(VARCHAR(50), nullable=False, comment='Dependencia')
    origen_movimiento = Column(VARCHAR(50), nullable=False, comment='Origen del movimiento')
    items = Column(JSON(True), nullable=False, comment='Items')
    nro_informe = Column(INTEGER, nullable=False, comment='Numero del informe')
    fecha_informe = Column(DATE, nullable=False, comment='Fecha del informe')
    observacion = Column(VARCHAR(10000), nullable=False, comment='Observacion')
    cont_informe = Column(INTEGER, nullable=False, comment='Contador del informe')
    sub_total = Column(DECIMAL(10, 2), nullable=False, comment='Sub total')
    iva = Column(DECIMAL(10, 2), nullable=False, comment='IVA')
    totales = Column(DECIMAL(10, 2), nullable=False, comment='Totales')
    cuenta = Column(VARCHAR(50), nullable=False, comment='Cuenta')


class ModelFC05(ModelBase):
    __tablename__ = 'informe_fc05'
    # __table_args__.update({'comment': 'Informe de la FC05'})
    fecha = Column(DATE, nullable=False, comment='Fecha')
    cuenta = Column(VARCHAR(50), nullable=False, comment='Cuenta')
    nombre_cuenta = Column(VARCHAR(50), nullable=False, comment='Nombre de la cuenta')
    valor_unitario = Column(DECIMAL(10, 2), nullable=False, comment='Valor unitario')
    origen = Column(VARCHAR(50), nullable=False, comment='Origen')
    saldo = Column(DECIMAL(10, 2), nullable=False, comment='Saldo')
    total = Column(DECIMAL(10, 2), nullable=False, comment='Total')
    numero_informe = Column(INTEGER, nullable=False, comment='Numero del informe')
    fecha_informe = Column(DATE, nullable=False, comment='Fecha del informe')
    month = Column(INTEGER, nullable=False, comment='Mes')
    year = Column(INTEGER, nullable=False, comment='Año')


class ModelFC06(ModelBase):
    __tablename__ = 'informe_fc06'
    # __table_args__.update({'comment': 'Informe de la FC06'})

    cuenta = Column(VARCHAR(50), nullable=False, comment='Cuenta')
    sub_cuenta = Column(VARCHAR(50), nullable=False, comment='Sub cuenta')
    nombre_cuenta = Column(VARCHAR(50), nullable=False, comment='Nombre de la cuenta')
    analitico = Column(VARCHAR(50), nullable=False, comment='Analitico')
    cantidad = Column(DECIMAL(10, 2), nullable=False, comment='Cantidad')
    valor_parcial = Column(DECIMAL(10, 2), nullable=False, comment='Valor parcial')
    valor_total = Column(DECIMAL(10, 2), nullable=False, comment='Valor total')
    unidad_jerarquica = Column(VARCHAR(50), nullable=False, comment='Unidad jerarquica')
    reparticion = Column(VARCHAR(50), nullable=False, comment='Reparticion')
    dependencia = Column(VARCHAR(50), nullable=False, comment='Dependencia')
    numero_informe = Column(INTEGER, nullable=False, comment='Numero del informe')
    fecha_informe = Column(DATE, nullable=False, comment='Fecha del informe')
    month = Column(INTEGER, nullable=False, comment='Mes')
    year = Column(INTEGER, nullable=False, comment='Año')


class ModelFC10(ModelBase):
    __tablename__ = 'informe_fc10'
    # __table_args__.update({'comment': 'Informe de la FC10'})
    entidad = Column(VARCHAR(50), nullable=False, comment='Entidad')
    entidad_text = Column(VARCHAR(50), nullable=False, comment='Entidad')
    unidad_jerarquica = Column(VARCHAR(50), nullable=False, comment='Unidad jerarquica')
    reparticion = Column(VARCHAR(50), nullable=False, comment='Reparticion')
    reparticion_text = Column(VARCHAR(50), nullable=False, comment='Reparticion')
    dependencia = Column(VARCHAR(50), nullable=False, comment='Dependencia')
    dependencia_text = Column(VARCHAR(50), nullable=False, comment='Dependencia')
    responsable = Column(VARCHAR(50), nullable=False, comment='Responsable')
    cargo = Column(VARCHAR(50), nullable=False, comment='Cargo')
    items = Column(JSON(True), nullable=False, comment='Items')
    fecha_informe = Column(DATE, nullable=False, comment='Fecha del informe')
    numero_informe = Column(INTEGER, nullable=False, comment='Numero del informe')
    cont_informe = Column(INTEGER, nullable=False, comment='Contador del informe')
    cuenta = Column(VARCHAR(50), nullable=False, comment='Cuenta')
    total = Column(DECIMAL(10, 2), nullable=False, comment='Total')
