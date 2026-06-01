from odoo import models, fields

class actor(models.Model):
    _name = 'videoclub.actor'
    _description = 'Describe la clase actor'

    name = fields.Char(string="Nombre", required=True)
    nacionalidad = fields.Char(string="Nacionalidad")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")

    pelicula_ids = fields.Many2many(
        'videoclub.pelicula'
    )