from sqlalchemy import text, TextClause

from core.extensions import ScriptObject


class Informe06ItemsScript(ScriptObject):

    def script(self) -> TextClause:
        query = """
        SELECT t.cuenta,t.nombre_cuenta,t.origen,t.fecha,sum(DISTINCT(t.valor_unitario)) as valor_total 
        FROM informe_fc05 t 
        where t.year=:year 
        GROUP BY t.cuenta
        order by 1,2,3,4 desc 
        """
        return text(query)
