from api_v2.conexion import repo_session
from api_v2.models import ModelContadores


def last_id(informe_name: str) -> int:
    """
    Buscar el siguiente id del informe especificado
    :param informe_name:
    :return:
    """
    if not informe_name:
        raise ValueError('El informe es requerido')

    with repo_session() as s:
        obj = s.query(ModelContadores) \
            .filter_by(informe=informe_name) \
            .order_by(ModelContadores.numero.desc()) \
            .limit(1) \
            .one_or_none()

        return 1 if obj is None else obj.numero


def next_id(informe_name: str) -> int:
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
            .order_by(ModelContadores.numero.desc()) \
            .limit(1) \
            .one_or_none()

        return 1 if obj is None else obj.numero + 1
