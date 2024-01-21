import re

from services_info.conexion import Conexion


def getfc03(id):
    connect = Conexion(f"select * from informefc03 where id={id};")
    filas = connect.res.fetchall()  # capturo las filas de datos
    columnas = connect.res.description  # capturo los nombres de columnas

    # objetivo crear una lista de diccionario con filas y columnas

    resultado = []  # lista para guadar diccionario

    for fila in filas:
        dato = {}  # diccionario para cada registro
        posicion = 0  # posicion de columna

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connect.con.close()

    return resultado


def select_ingreso():
    connectSelectIngreso = Conexion("SELECT sum(quantity) FROM movements WHERE quantity>0")
    resultado = connectSelectIngreso.res.fetchall()
    connectSelectIngreso.con.close()
    return resultado[0][0]


def select_egreso():
    connectSelectEgreso = Conexion("SELECT sum(quantity) FROM movements WHERE quantity<0")
    resultado = connectSelectEgreso.res.fetchall()
    connectSelectEgreso.con.close()
    return resultado[0][0]


def select_all_contador():
    connect = Conexion("select id,informe,numero,fecha from contadores order by fecha;")
    filas = connect.res.fetchall()  # capturo las filas de datos
    columnas = connect.res.description  # capturo los nombres de columnas

    # objetivo crear una lista de diccionario con filas y columnas

    resultado = []  # lista para guadar diccionario

    for fila in filas:
        dato = {}  # diccionario para cada registro
        posicion = 0  # posicion de columna

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connect.con.close()

    return resultado


def insert_contador(registro):
    """Registrar el contador"""
    connectInsert = Conexion("insert into contadores(informe,numero,fecha) values(?,?,?)", registro)
    connectInsert.con.commit()  # funcion que registra finalmente
    connectInsert.con.close()


def select_informe_fc03_by_date(date_init):
    connectSelectfc03 = Conexion(f"select * from informefc03 where fecha_informe='{date_init}'")
    filas = connectSelectfc03.res.fetchall()  # capturo las filas de datos
    columnas = connectSelectfc03.res.description  # capturo los nombres de columnas

    # objetivo crear una lista de diccionario con filas y columnas

    resultado = []  # lista para guadar diccionario

    for fila in filas:
        dato = {}  # diccionario para cada registro
        posicion = 0  # posicion de columna

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connectSelectfc03.con.close()

    return resultado


def select_informe_fc03_all():
    connectSelectfc03 = Conexion(f"select * from informefc03 order by id desc")
    filas = connectSelectfc03.res.fetchall()  # capturo las filas de datos
    columnas = connectSelectfc03.res.description  # capturo los nombres de columnas

    # objetivo crear una lista de diccionario con filas y columnas

    resultado = []  # lista para guadar diccionario

    for fila in filas:
        dato = {}  # diccionario para cada registro
        posicion = 0  # posicion de columna

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connectSelectfc03.con.close()

    return resultado


def select_informe_fc04_all():
    connectSelectfc04 = Conexion(f"select * from informefc04 order by id desc")
    filas = connectSelectfc04.res.fetchall()  # capturo las filas de datos
    columnas = connectSelectfc04.res.description  # capturo los nombres de columnas

    # objetivo crear una lista de diccionario con filas y columnas

    resultado = []  # lista para guadar diccionario

    for fila in filas:
        dato = {}  # diccionario para cada registro
        posicion = 0  # posicion de columna

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connectSelectfc04.con.close()

    return resultado


def select_informe_fc05_all():
    connectSelectfc05 = Conexion(f"select * from informefc05 order by id desc")
    filas = connectSelectfc05.res.fetchall()  # capturo las filas de datos
    columnas = connectSelectfc05.res.description  # capturo los nombres de columnas

    # objetivo crear una lista de diccionario con filas y columnas

    resultado = []  # lista para guadar diccionario

    for fila in filas:
        dato = {}  # diccionario para cada registro
        posicion = 0  # posicion de columna

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connectSelectfc05.con.close()

    return resultado


def select_informe_fc05_items(m, y):
    # connectSelectfc05item = Conexion(f"SELECT T1.cuenta,T1.nombre_cuenta,T1.origen,T1.fecha,sum(DISTINCT(valor_unitario)) as valor_total FROM informefc05 T1 where month={m} and year={y} GROUP BY T1.cuenta ORDER BY fecha desc;")
    connectSelectfc05item = Conexion(
        f"SELECT T1.cuenta,T1.nombre_cuenta,T1.origen,T1.fecha,sum(DISTINCT(T2.valor_unitario)) as saldo_anterior, sum(DISTINCT(T1.valor_unitario)) as valor_total, ( sum(DISTINCT(T1.valor_unitario))+ sum(DISTINCT(T2.valor_unitario))) as valor_final FROM informefc05 as T1,informefc05 as T2 where T1.cuenta=T2.cuenta and (CASE WHEN T1.valor_unitario==0.0 THEN (T2.month <= {m} and T2.year={y}) AND (T1.month={m} and T1.year={y}) ELSE (T2.month < {m} and T2.year={y}) AND (T1.month={m} and T1.year={y})  END) GROUP BY T1.cuenta ORDER BY T1.cuenta asc;")
    filas = connectSelectfc05item.res.fetchall()  # capturo las filas de datos
    columnas = connectSelectfc05item.res.description  # capturo los nombres de columnas

    # objetivo crear una lista de diccionario con filas y columnas

    resultado = []  # lista para guadar diccionario

    for fila in filas:
        dato = {}  # diccionario para cada registro
        posicion = 0  # posicion de columna

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connectSelectfc05item.con.close()

    return resultado


def select_informe_fc05_sum(month, year):
    connectSelectfc05sum = Conexion(
        f"select sum(valor_unitario) as total from informefc05 where month={month} and year={year};")
    filas = connectSelectfc05sum.res.fetchall()  # capturo las filas de datos

    return filas[0][0]


def select_informe_fc06_items(y):
    connectSelectfc06item = Conexion(
        f"SELECT T1.cuenta,T1.nombre_cuenta,T1.origen,T1.fecha,sum(DISTINCT(valor_unitario)) as valor_total FROM informefc05 T1 where year={y} GROUP BY T1.cuenta ORDER BY fecha desc;")
    filas = connectSelectfc06item.res.fetchall()  # capturo las filas de datos
    columnas = connectSelectfc06item.res.description  # capturo los nombres de columnas

    # objetivo crear una lista de diccionario con filas y columnas

    resultado = []  # lista para guadar diccionario

    for fila in filas:
        dato = {}  # diccionario para cada registro
        posicion = 0  # posicion de columna

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connectSelectfc06item.con.close()

    return resultado


def select_informe_fc06_sum(year):
    connectSelectfc06sum = Conexion(f"select sum(valor_unitario) as total from informefc05 where year={year};")
    filas = connectSelectfc06sum.res.fetchall()  # capturo las filas de datos

    return filas[0][0]


def select_informe_fc04_items():
    connectSelectfc04 = Conexion(f"select items from informefc04")
    filas = connectSelectfc04.res.fetchall()  # capturo las filas de datos

    # objetivo crear una lista de diccionario con filas y columnas

    resultado = []  # lista para guadar diccionario

    for fila in filas:
        resultado.append(fila)
        resultado += resultado

    connectSelectfc04.con.close()
    new_file = re.sub("\[|\]|\(|\)", "", str(filas))
    sample_str = re.sub(".$", "", new_file)
    sample_str = sample_str.replace("',, '", ",")
    return sample_str


def select_informe_fc10_all():
    connectSelectfc10 = Conexion(f"select * from informefc10 order by id desc")
    filas = connectSelectfc10.res.fetchall()  # capturo las filas de datos
    columnas = connectSelectfc10.res.description  # capturo los nombres de columnas

    # objetivo crear una lista de diccionario con filas y columnas

    resultado = []  # lista para guadar diccionario

    for fila in filas:
        dato = {}  # diccionario para cada registro
        posicion = 0  # posicion de columna

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connectSelectfc10.con.close()

    return resultado


def insert_informe_fc03(registro):
    connectInsert = Conexion(
        "insert into informefc03(entidad,unidad_jerarquica,reparticion,dependencia,area,origen," +
        "cuenta,sub_cuenta,analitico_1,analitico_2,descripcion,fecha,tipo,numero,rotulado,cantidad,valor_unitario," +
        "valor_total,signo,fecha_incorp,vida_util,origen_movi,sub_total,iva,totales,numero_informe,fecha_informe,items,reparticion_cod,dependencia_cod,cont_informe)" +
        " values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", registro)
    connectInsert.con.commit()
    connectInsert.con.close()


def insert_informe_fc04(registro):
    connectInsertFc04 = Conexion(
        "insert into informefc04(unidad_jerarquica,entidad,entidad_text,reparticion,reparticion_text," +
        "dependencia,origen_movimiento,items,nro_informe,fecha_informe,observacion,cont_informe,sub_total,iva,totales,cuenta)" +
        " values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", registro)
    connectInsertFc04.con.commit()
    connectInsertFc04.con.close()


def insert_informe_fc10(registro):
    connectInsertFc10 = Conexion(
        "insert into informefc10(entidad,entidad_text,unidad_jerarquica,reparticion,reparticion_text," +
        "dependencia,dependencia_text,responsable,cargo,items,fecha_informe,numero_informe,cont_informe,cuenta,total)" +
        " values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", registro)
    connectInsertFc10.con.commit()
    connectInsertFc10.con.close()


def select_informe_fc05_by_date(date_init):
    connectSelectfc05 = Conexion(f"select * from informefc05 where fecha='{date_init}'")
    filas = connectSelectfc05.res.fetchall()  # capturo las filas de datos
    columnas = connectSelectfc05.res.description  # capturo los nombres de columnas

    # objetivo crear una lista de diccionario con filas y columnas

    resultado = []  # lista para guadar diccionario

    for fila in filas:
        dato = {}  # diccionario para cada registro
        posicion = 0  # posicion de columna

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connectSelectfc05.con.close()

    return resultado


def insert_informe_fc05(registro):
    connectInsertfc05 = Conexion(
        "insert into informefc05(fecha,cuenta,nombre_cuenta,valor_unitario,origen,saldo,total,numero_informe,fecha_informe,month,year)" +
        " values(?,?,?,?,?,?,?,?,?,?,?)", registro)
    connectInsertfc05.con.commit()
    connectInsertfc05.con.close()


def select_informe_fc06_by_date(date_init):
    connectSelectfc06 = Conexion(f"select * from informefc06 where fecha_informe='{date_init}'")
    filas = connectSelectfc06.res.fetchall()  # capturo las filas de datos
    columnas = connectSelectfc06.res.description  # capturo los nombres de columnas

    # objetivo crear una lista de diccionario con filas y columnas

    resultado = []  # lista para guadar diccionario

    for fila in filas:
        dato = {}  # diccionario para cada registro
        posicion = 0  # posicion de columna

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connectSelectfc06.con.close()

    return resultado


def insert_informe_fc06(registro):
    connectInsertfc06 = Conexion(
        "insert into informefc06(cuenta,sub_cuenta,nombre_cuenta,analitico," +
        "cantidad,valor_parcial,valor_total,unidad_jerarquica,reparticion,dependencia," +
        "numero_informe,fecha_informe) values(?,?,?,?,?,?,?,?,?,?,?,?)", registro)
    connectInsertfc06.con.commit()
    connectInsertfc06.con.close()


def select_contador_by(informe_tag):
    """seleccionar el ultimo valor de un contador"""
    connectSelectBy = Conexion(
        f'SELECT numero from contadores WHERE informe="{informe_tag}" ORDER BY numero DESC LIMIT 1;')
    resultado = connectSelectBy.res.fetchall()
    connectSelectBy.con.close()
    return resultado


def delete_by(id):
    """Borrar movimientos"""
    connectDeleteBy = Conexion(f"delete from movements where id={id}")
    connectDeleteBy.con.commit()
    connectDeleteBy.con.close()


def update_by(id, registro):  # ['date','concept','quantity']
    """Actualizar movimientos"""
    connectUpdate = Conexion(f"UPDATE movements SET date=?,concept=?,quantity=? WHERE id={id}", registro)
    connectUpdate.con.commit()
    connectUpdate.con.close()


def select_year_contador_by(num):
    connectSelectYearBy = Conexion(
        f'SELECT strftime("%Y", fecha) as year from contadores WHERE informe="{num}" ORDER BY id DESC LIMIT 1;')
    resultado = connectSelectYearBy.res.fetchall()
    connectSelectYearBy.con.close()
    return resultado
