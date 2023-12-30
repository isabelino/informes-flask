import datetime

from sqlalchemy.exc import DatabaseError

from api_v2.conexion import repo_session
from api_v2.loggers import logger
from api_v2.models import ModelContadores


def last_id(informe_name: str) -> int:
    """
    Buscar el ultimo id del informe especificado
    :param informe_name:
    :return:
    """
    if not informe_name:
        raise ValueError('El informe es requerido')

    with repo_session() as s:
        obj = s.query(ModelContadores) \
            .filter_by(informe=informe_name) \
            .order_by(ModelContadores.numero.desc()).limit(1).one_or_none()

        if obj:
            logger.info(f'Ultimo id {obj.numero} de {obj.informe}')
            nobj = ModelContadores()
            nobj.informe = informe_name
            nobj.numero = obj.numero + 1
            nobj.fecha = datetime.date.today().isoformat()
            try:
                s.add(nobj)
            except DatabaseError as e:
                logger.error(repr(e))
                s.rollback()
            else:
                s.commit()
            finally:
                s.flush()
            logger.debug(nobj.as_dict())
            return nobj.numero
        else:
            logger.info(f'Nuevo id de {informe_name} es 1')
            obj = ModelContadores()
            obj.numero = 1
            obj.informe = informe_name
            obj.fecha = datetime.date.today().isoformat()
            try:
                s.add(obj)
            except DatabaseError as e:
                logger.error(repr(e))
                s.rollback()
            else:
                logger.success(obj.as_dict())
                s.commit()
            logger.debug(obj.as_dict())
            return obj.numero
