import json
import sqlite3
from datetime import date, datetime
from http import HTTPStatus

from flask import jsonify, render_template, request

from services_info.models import *


class Routes:
    def __init__(self, app):

        @app.route("/")
        def init_api():
            """
            Home page
            :return:
            """
            return render_template('index.html')

        @app.route(f"/api/{VERSION}/prueba/<id>")
        def pruebafc03(id):
            """
            trae el registro de fc03
            :param id:
            :return:
            """

            try:
                registros = getfc03(id)
                # return jsonify(registros)
                return jsonify(
                    {
                        "data": registros,
                        "status": "OK"
                    }
                ), HTTPStatus.OK  # agrego codigo de respuesta http
            except sqlite3.Error as e:
                return jsonify(
                    {
                        "data": str(e),
                        "status": "Error"
                    }
                ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        # @app.route(f"/api/{VERSION}/fc03/all")
        # def all_fc03_items():
        #     try:
        #         registros = select_informe_fc03_all()
        #         # return jsonify(registros)
        #         return jsonify(
        #             {
        #                 "data": registros,
        #                 "status": "OK"
        #             }
        #         ), HTTPStatus.OK  # agrego codigo de respuesta http
        #     except sqlite3.Error as e:
        #         return jsonify(
        #             {
        #                 "data": str(e),
        #                 "status": "Error"
        #             }
        #         ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        # @app.route(f"/api/{VERSION}/fc04/all")
        # def all_fc04_items():
        #     try:
        #         registros = select_informe_fc04_all()
        #         # return jsonify(registros)
        #         return jsonify(
        #             {
        #                 "data": registros,
        #                 "status": "OK"
        #             }
        #         ), HTTPStatus.OK  # agrego codigo de respuesta http
        #     except sqlite3.Error as e:
        #         return jsonify(
        #             {
        #                 "data": str(e),
        #                 "status": "Error"
        #             }
        #         ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        # @app.route(f"/api/{VERSION}/fc05/all")
        # def all_fc05_items():
        #     try:
        #         registros = select_informe_fc05_all()
        #         # return jsonify(registros)
        #         return jsonify(
        #             {
        #                 "data": registros,
        #                 "status": "OK"
        #             }
        #         ), HTTPStatus.OK  # agrego codigo de respuesta http
        #     except sqlite3.Error as e:
        #         return jsonify(
        #             {
        #                 "data": str(e),
        #                 "status": "Error"
        #             }
        #         ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        # @app.route(f"/api/{VERSION}/fc05/items/<m>/<y>")
        # def fc05_items(m, y):
        #     try:
        #         registros = select_informe_fc05_items(m, y)
        #         # return jsonify(registros)
        #         return jsonify(
        #             {
        #                 "data": registros,
        #                 "status": "OK"
        #             }
        #         ), HTTPStatus.OK  # agrego codigo de respuesta http
        #     except sqlite3.Error as e:
        #         return jsonify(
        #             {
        #                 "data": str(e),
        #                 "status": "Error"
        #             }
        #         ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        # @app.route(f"/api/{VERSION}/fc06/items/<y>")
        # def fc06_items(y):
        #     try:
        #         registros = select_informe_fc06_items(y)
        #         # return jsonify(registros)
        #         return jsonify(
        #             {
        #                 "data": registros,
        #                 "status": "OK"
        #             }
        #         ), HTTPStatus.OK  # agrego codigo de respuesta http
        #     except sqlite3.Error as e:
        #         return jsonify(
        #             {
        #                 "data": str(e),
        #                 "status": "Error"
        #             }
        #         ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        @app.route(f"/api/{VERSION}/fc06/sumitem/<y>")
        def all_fc06_items_sum(y):
            try:
                registros = select_informe_fc06_sum(y)
                # return jsonify(registros)
                return jsonify(
                    {
                        "data": registros,
                        "status": "OK"
                    }
                ), HTTPStatus.OK  # agrego codigo de respuesta http
            except sqlite3.Error as e:
                return jsonify(
                    {
                        "data": str(e),
                        "status": "Error"
                    }
                ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        @app.route(f"/api/{VERSION}/fc05/sumitem/<m>/<y>")
        def all_fc05_items_sum(m, y):
            try:
                registros = select_informe_fc05_sum(m, y)
                # return jsonify(registros)
                return jsonify(
                    {
                        "data": registros,
                        "status": "OK"
                    }
                ), HTTPStatus.OK  # agrego codigo de respuesta http
            except sqlite3.Error as e:
                return jsonify(
                    {
                        "data": str(e),
                        "status": "Error"
                    }
                ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        @app.route(f"/api/{VERSION}/fc04/items")
        def all_fc04_items_alone():
            try:
                registros = select_informe_fc04_items()
                return jsonify(registros)
                '''
                return jsonify(
                    {
                        "data": registros,
                        "status": "OK"
                    }
                ),HTTPStatus.OK #agrego codigo de respuesta http
                '''
            except sqlite3.Error as e:
                return jsonify(
                    {
                        "data": str(e),
                        "status": "Error"
                    }
                ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        @app.route(f"/api/{VERSION}/fc10/all")
        def all_fc10_items():
            try:
                registros = select_informe_fc10_all()
                # return jsonify(registros)
                return jsonify(
                    {
                        "data": registros,
                        "status": "OK"
                    }
                ), HTTPStatus.OK  # agrego codigo de respuesta http
            except sqlite3.Error as e:
                return jsonify(
                    {
                        "data": str(e),
                        "status": "Error"
                    }
                ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        # @app.route(f"/api/{VERSION}/contadores")
        # def all_movements():
        #
        #     try:
        #         registros = select_all_contador()
        #         # return jsonify(registros)
        #         return jsonify(
        #             {
        #                 "data": registros,
        #                 "status": "OK"
        #             }
        #         ), HTTPStatus.OK  # agrego codigo de respuesta http
        #     except sqlite3.Error as e:
        #         return jsonify(
        #             {
        #                 "data": str(e),
        #                 "status": "Error"
        #             }
        #         ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        # mostrar ultimo numero de informe
        # @app.route(f"/api/{VERSION}/contador/<num>")
        # def contador_by_numero(num):
        #
        #     try:
        #         registros = select_contador_by(num)
        #         if len(registros) == 0:
        #             registros = [[0]]
        #         return jsonify(
        #             {
        #                 "data": registros[0][0]
        #             }
        #         ), HTTPStatus.OK  # agrego codigo de respuesta http
        #     except sqlite3.Error as e:
        #         return jsonify(
        #             {
        #                 "data": str(e),
        #                 "status": "Error"
        #             }
        #         ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        # crear nuevo registro de contador de informe
        # @app.route(f"/api/{VERSION}/contador/new", methods=["POST"])
        # def add_contador():
        #     registro = request.json
        #     try:
        #         hoy = date.today().isoformat()
        #         ultimo_numero_list = select_contador_by(registro['informe'])
        #         ultimo_numero = 0
        #         if len(ultimo_numero_list) == 0:
        #             ultimo_numero = 1
        #         else:
        #             ultimo_numero = ultimo_numero_list[0][0] + 1
        #
        #         insert_contador([registro['informe'], ultimo_numero, hoy])
        #         return jsonify(
        #             {
        #                 "status": "OK"
        #             }
        #         ), HTTPStatus.CREATED  # agrego codigo de respuesta http
        #     except sqlite3.Error as e:
        #         return jsonify(
        #             {
        #                 "data": str(e),
        #                 "status": "Error"
        #             }
        #         ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        # mostar registros de fc03 por fecha
        # @app.route(f"/api/{VERSION}/fc03/date/<date>")
        # def fc03_by_date(date):
        #
        #     try:
        #         registros = select_informe_fc03_by_date(date)
        #         return jsonify(
        #             {
        #                 "data": registros,
        #                 "status": "OK"
        #             }
        #         ), HTTPStatus.OK  # agrego codigo de respuesta http
        #     except sqlite3.Error as e:
        #         return jsonify(
        #             {
        #                 "data": str(e),
        #                 "status": "Error"
        #             }
        #         ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        # crear nuevo registro de fc03
        @app.route(f"/api/{VERSION}/fc03/new", methods=["POST"])
        def add_informe_fc03():
            registro = request.json
            print("esto recibo", registro)
            try:
                hoy = date.today().isoformat()
                ultimo_numero_list = select_contador_by('fc03')
                ultimo_numero = 0
                if len(ultimo_numero_list) == 0:
                    ultimo_numero = 1
                else:
                    ultimo_numero = ultimo_numero_list[0][0] + 1

                insert_contador(['fc03', ultimo_numero, hoy])

                items = [{'cuenta': '26112', 'subcuenta': '1', 'analitico1': '9', 'analitico2': '99',
                          'descripcion': "Muebles y enseres \nmobiliarios y enseres de oficina \nEscritorios \notros tipos de escritorio\nMESA DE MADERA CLASSIC MOBLES {10643}",
                          'fecha_adquisicion': '20-12-2018', 'rotulado': '18-6-3-1224', 'cantidad': '1',
                          'valor_unitario': '363.636', 'valor_total': '363.636', 'bienes': '',
                          'estado_conservacion': 'B.', 'diferencia_libro': '', 'observacion': ''},
                         {'cuenta': '26112', 'subcuenta': '1', 'analitico1': '9', 'analitico2': '99',
                          'descripcion': "Muebles y enseres \nmobiliarios y enseres de oficina \nEscritorios \notros tipos de escritorio\nMESA DE MADERA CLASSIC MOBLES {10643}",
                          'fecha_adquisicion': '20-12-2018', 'rotulado': '18-6-3-1224', 'cantidad': '1',
                          'valor_unitario': '363.636', 'valor_total': '363.636', 'bienes': '',
                          'estado_conservacion': 'B.', 'diferencia_libro': '', 'observacion': ''},
                         {'cuenta': '26112', 'subcuenta': '1', 'analitico1': '9', 'analitico2': '99',
                          'descripcion': "Muebles y enseres \nmobiliarios y enseres de oficina \nEscritorios \notros tipos de escritorio\nMESA DE MADERA CLASSIC MOBLES {10643}",
                          'fecha_adquisicion': '20-12-2018', 'rotulado': '18-6-3-1224', 'cantidad': '1',
                          'valor_unitario': '363.636', 'valor_total': '363.636', 'bienes': '',
                          'estado_conservacion': 'B.', 'diferencia_libro': '', 'observacion': ''}
                         ]
                # json to string
                items_str = json.dumps(items, ensure_ascii=False)

                insert_informe_fc03([
                    registro['entidad'], registro['unidad_jerarquica'], registro['reparticion'],
                    registro['dependencia'], registro['area'], registro['origen'],
                    registro['cuenta'], registro['sub_cuenta'], registro['analitico_1'],
                    registro['analitico_2'], registro['descripcion'], registro['fecha'],
                    registro['tipo'], registro['numero'], registro['rotulado'],
                    registro['cantidad'], registro['valor_unitario'], registro['valor_total'],
                    registro['signo'], registro['fecha_incorp'], registro['vida_util'],
                    registro['origen_movi'], registro['sub_total'], registro['iva'],
                    registro['totales'], registro['numero_informe'], hoy, registro['items'],
                    registro['reparticion_cod'], registro['dependencia_cod'], ultimo_numero
                ])
                return jsonify(
                    {
                        "status": "OK"
                    }
                ), HTTPStatus.CREATED  # agrego codigo de respuesta http
            except sqlite3.Error as e:
                return jsonify(
                    {
                        "data": str(e),
                        "status": "Error"
                    }
                ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        # crear nuevo registro de fc04
        @app.route(f"/api/{VERSION}/fc04/new", methods=["POST"])
        def add_informe_fc04():
            registro = request.json
            print("esto recibo", registro)
            try:
                hoy = date.today().isoformat()
                ultimo_numero_list = select_contador_by('fc04')
                ultimo_numero = 0
                if len(ultimo_numero_list) == 0:
                    ultimo_numero = 1
                else:
                    ultimo_numero = ultimo_numero_list[0][0] + 1

                insert_contador(['fc04', ultimo_numero, hoy])

                items = [{'cuenta': '26112', 'subcuenta': '\n 03', 'analitico1': '\n \n 99', 'analitico2': '04',
                          'descripcion': "Muebles y enseres \nequipos de eseo y seguridad\nOtros equipos y mubles de AHS\nOtros tipos de enceradoras electricas\nAPARATO DIFUSOR SPHIRUS{11648}",
                          'fecha_adquisicion': '01-10-2019', 'tipo': 'factura', 'nro': '01', 'rotulado': '18-6-3-1224',
                          'cantidad': '1', 'valor_unitario': '59.091', 'valor_total': '59.091', 'signo': 'signo',
                          'fecha_incorp': '10-10-2019', 'vida_util': '10', 'origen_movimento': 'C'},
                         {'cuenta': '26112', 'subcuenta': '\n 03', 'analitico1': '\n \n 99', 'analitico2': '04',
                          'descripcion': "Muebles y enseres \nequipos de eseo y seguridad\nOtros equipos y mubles de AHS\nOtros tipos de enceradoras electricas\nAPARATO DIFUSOR SPHIRUS{11648}",
                          'fecha_adquisicion': '01-10-2019', 'tipo': 'factura', 'nro': '01', 'rotulado': '18-6-3-1224',
                          'cantidad': '1', 'valor_unitario': '59.091', 'valor_total': '59.091', 'signo': 'signo',
                          'fecha_incorp': '10-10-2019', 'vida_util': '10', 'origen_movimento': 'C'}
                         ]
                # json to string
                items_str = json.dumps(items, ensure_ascii=False)
                # print("esto es items",items_str)
                print("esto es ultimo numero", ultimo_numero)
                insert_informe_fc04([
                    registro['unidad_jerarquica'], registro['entidad'],
                    registro['entidad_text'], registro['reparticion'], registro['reparticion_text'],
                    registro['dependencia'], registro['origen_movimiento'], registro['items'],
                    registro['nro_informe'], hoy, registro['observacion'], ultimo_numero,
                    registro['sub_total'], registro['iva'], registro['totales'], registro['cuenta']
                ])
                return jsonify(
                    {
                        "status": "OK"
                    }
                ), HTTPStatus.CREATED  # agrego codigo de respuesta http
            except sqlite3.Error as e:
                return jsonify(
                    {
                        "data": str(e),
                        "status": "Error"
                    }
                ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        # crear nuevo registro de fc04
        @app.route(f"/api/{VERSION}/fc10/new", methods=["POST"])
        def add_informe_fc10():
            registro = request.json
            # print("esto recibo",registro)
            try:
                hoy = date.today().isoformat()
                year = datetime.now().strftime('%Y')
                ultimo_numero_list = select_contador_by('fc10')
                ultimo_numero = 0
                numero_informe = ""
                if len(ultimo_numero_list) == 0:
                    ultimo_numero = 1
                else:
                    ultimo_numero = ultimo_numero_list[0][0] + 1

                insert_contador(['fc10', ultimo_numero, hoy])

                numero_informe = str(ultimo_numero) + "/" + str(year)

                insert_informe_fc10([
                    registro['entidad'], registro['entidad_text'], registro['unidad_jerarquica'],
                    registro['reparticion'], registro['reparticion_text'], registro['dependencia'],
                    registro['dependencia_text'], registro['responsable'], registro['cargo'],
                    registro['items'], hoy, numero_informe, ultimo_numero, registro['cuenta'], registro['total']
                ])
                return jsonify(
                    {
                        "status": "OK"
                    }
                ), HTTPStatus.CREATED  # agrego codigo de respuesta http
            except sqlite3.Error as e:
                return jsonify(
                    {
                        "data": str(e),
                        "status": "Error"
                    }
                ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        # crear nuevo registro de fc05 por fecha
        # @app.route(f"/api/{VERSION}/fc05/date/<date>")
        # def fc05_by_date(date):
        #
        #     try:
        #         registros = select_informe_fc05_by_date(date)
        #         return jsonify(
        #             {
        #                 "data": registros,
        #                 "status": "OK"
        #             }
        #         ), HTTPStatus.OK
        #     except sqlite3.Error as e:
        #         return jsonify(
        #             {
        #                 "data": str(e),
        #                 "status": "Error"
        #             }
        #         ), HTTPStatus.BAD_REQUEST

        # crear nuevo registro de fc05
        @app.route(f"/api/{VERSION}/fc05/new", methods=["POST"])
        def add_informe_fc05():
            registro = request.json
            try:
                hoy = date.today().isoformat()
                # ultimo_numero_list = select_contador_by('fc05')
                ultimo_numero = 0
                # if len(ultimo_numero_list) == 0:
                #    ultimo_numero = 1
                # else:
                #    ultimo_numero = ultimo_numero_list[0][0] + 1

                insert_contador(['fc05', ultimo_numero, hoy])
                insert_informe_fc05([
                    registro['fecha'], registro['cuenta'], registro['nombre_cuenta'],
                    registro['valor_unitario'], registro['origen'], registro['saldo'], registro['total'], ultimo_numero,
                    hoy, str(datetime.today().month), str(datetime.today().year)
                ])
                return jsonify(
                    {
                        "status": "OK"
                    }
                ), HTTPStatus.CREATED
            except sqlite3.Error as e:
                return jsonify(
                    {
                        "data": str(e),
                        "status": "Error"
                    }
                ), HTTPStatus.BAD_REQUEST

        # crear nuevo registro de fc06
        @app.route(f"/api/{VERSION}/fc06/date/<date>")
        def fc06_by_date(date):

            try:
                registros = select_informe_fc06_by_date(date)
                return jsonify(
                    {
                        "data": registros,
                        "status": "OK"
                    }
                ), HTTPStatus.OK
            except sqlite3.Error as e:
                return jsonify(
                    {
                        "data": str(e),
                        "status": "Error"
                    }
                ), HTTPStatus.BAD_REQUEST

        # crear nuevo registro de fc05
        @app.route(f"/api/{VERSION}/fc06/new", methods=["POST"])
        def add_informe_fc06():
            registro = request.json
            try:
                hoy = date.today().isoformat()
                ultimo_numero_list = select_contador_by('fc06')
                ultimo_numero = 0
                if len(ultimo_numero_list) == 0:
                    ultimo_numero = 1
                else:
                    ultimo_numero = ultimo_numero_list[0][0] + 1

                insert_contador(['fc06', ultimo_numero, hoy])
                insert_informe_fc06([
                    registro['cuenta'], registro['sub_cuenta'], registro['nombre_cuenta'],
                    registro['analitico'], registro['cantidad'], registro['valor_parcial'],
                    registro['valor_total'], registro['unidad_jerarquica'], registro['reparticion'],
                    registro['dependencia'], ultimo_numero, hoy
                ])
                return jsonify(
                    {
                        "status": "OK"
                    }
                ), HTTPStatus.CREATED
            except sqlite3.Error as e:
                return jsonify(
                    {
                        "data": str(e),
                        "status": "Error"
                    }
                ), HTTPStatus.BAD_REQUEST

        @app.route(f"/api/{VERSION}/update/<int:id>", methods=["PUT"])
        def update(id):
            registro = request.json
            try:
                update_by(id, [registro['date'], registro['concept'], registro['quantity']])
                return jsonify(
                    {
                        "status": "OK"
                    }
                ), HTTPStatus.CREATED  # agrego codigo de respuesta http
            except sqlite3.Error as e:
                return jsonify(
                    {
                        "data": str(e),
                        "status": "Error"
                    }
                ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http

        @app.route(f"/api/{VERSION}/delete/<int:id>", methods=["DELETE"])
        def remove(id):
            try:
                delete_by(id)
                return jsonify(
                    {
                        "status": "OK"
                    }
                ), HTTPStatus.OK  # agrego codigo de respuesta http
            except sqlite3.Error as e:
                return jsonify(
                    {
                        "data": str(e),
                        "status": "Error"
                    }
                ), HTTPStatus.BAD_REQUEST  # agrego codigo de respuesta http
