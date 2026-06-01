from odoo import models, fields

class categoria(models.Model):
    _name = 'videoclub.categoria'
    _description = 'Describe la clase categoria'

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")

    pelicula_ids = fields.One2many(
        'videoclub.pelicula',
        'categoria_id'
    )