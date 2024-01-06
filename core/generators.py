import datetime

from api_v2.conexion import repo_session
from api_v2.models import ModelContadores


def last_report_id(informe_name: str) -> int:
    """
    Buscar el siguiente id del informe especificado
    :param informe_name:
    :return:
    """
    if not informe_name:
        raise ValueError('El informe es requerido')

    with repo_session() as s:
        obj = s \
            .query(ModelContadores) \
            .filter_by(informe=informe_name) \
            .order_by(ModelContadores.numero.desc()) \
            .limit(1) \
            .one_or_none()

        value = 0 if obj is None else obj.numero

        # save position
        obj = ModelContadores()
        obj.informe = informe_name
        obj.fecha = datetime.date.today().isoformat()
        obj.numero = value + 1
        s.add(obj)
        s.commit()

        return value


def post_report_id(informe_name: str, value: int):
    """
    Registrar el siguiente id del informe especificado
    :param informe_name:
    :param value:
    :return:
    """
    with repo_session() as s:
        obj = ModelContadores()
        obj.informe = informe_name
        obj.fecha = datetime.date.today().isoformat()
        obj.numero = value
        s.add(obj)
        s.commit()
