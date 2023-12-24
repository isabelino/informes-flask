from sqlalchemy.sql.operators import desc_op

from api_v2.conexion import repo, repo_session
from api_v2.models import ModelContadores


def last_id(informe_name:str)->int:
    """
    Buscar el ultimo id del informe especificado
    :param informe_name:
    :return:
    """
    if not informe_name:
        raise ValueError('El informe es requerido')


    with repo_session() as s:

        obj = s.query(ModelContadores).filter_by(informe=informe_name).order_by(
            desc_op(ModelContadores.id)).first()

        return obj.numero + 1 if obj is not None else 1
