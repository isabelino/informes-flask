from core.extensions import ScriptObject


class Informe06ItemsScript(ScriptObject):

    def script(self) -> str:
        return """
        SELECT t.cuenta,t.nombre_cuenta,t.origen,t.fecha,sum(DISTINCT(valor_unitario)) as valor_total 
        FROM informefc05 t where year=:year 
        GROUP BY t.cuenta ORDER BY t.fecha desc    
        """
