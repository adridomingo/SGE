from odoo import http
from odoo.http import request
import json


class VideoClubAPI(http.Controller):

    # POST Y PUT
    @http.route('/videoclub/<model>', auth='none', cors=False, csrf=False,
                methods=["POST", "PUT"], type='http')
    def apiPostPut(self, **args):
        modelo = args['model']
        dicDatos = json.loads(args['data'])

        # Buscamos por name como clave
        if dicDatos.get("name"):
            buscado = [('name', '=', dicDatos["name"])]
        else:
            return "{'estado': 'Campo name no proporcionado'}"

        # POST
        if http.request.httprequest.method == 'POST':
            record = request.env[modelo].sudo().create(dicDatos)
            return http.Response(
                json.dumps(record.read(), default=str),
                status=200,
                mimetype='application/json'
            )

        # PUT
        if http.request.httprequest.method == 'PUT':
            record = request.env[modelo].sudo().search(buscado)
            if record and record[0]:
                record[0].write(dicDatos)
                return http.Response(
                    json.dumps(record.read(), default=str),
                    status=200,
                    mimetype='application/json'
                )
            return "Registro no encontrado"

        return http.request.env['ir.http'].session_info()


    # GET Y DELETE
    @http.route('/videoclub/get/<model>', auth='none', cors=False, csrf=False,
                methods=["GET", "DELETE"], type='http')
    def apiGetDelete(self, **args):
        modelo = args['model']
        dicDatos = json.loads(args['data'])
        buscado = []

        # Buscamos por name
        if dicDatos.get("name"):
            buscado = [('name', '=', dicDatos["name"])]
        else:
            return "{'estado': 'Campo name no proporcionado'}"

        # GET
        if http.request.httprequest.method == 'GET':
            record = request.env[modelo].sudo().search(buscado)
            if record and record[0]:
                return http.Response(
                    json.dumps(record.read(), default=str),
                    status=200,
                    mimetype='application/json'
                )
            return "Registro no encontrado"

        # DELETE
        if http.request.httprequest.method == 'DELETE':
            record = request.env[modelo].sudo().search(buscado)
            if record and record[0]:
                datos = http.Response(
                    json.dumps(record.read(), default=str),
                    status=200,
                    mimetype='application/json'
                )
                record[0].unlink()
                return datos
            return "Registro no encontrado"

        return http.request.env['ir.http'].session_info()