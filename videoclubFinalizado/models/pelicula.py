from odoo import models, fields, api

class pelicula(models.Model):
    _name='videoclub.pelicula'
    _description='Describe a la clase pelicula'

    _sql_constraints = [('unique_movie_name', 'unique(name)', 'El título de la película debe ser único')]

    name = fields.Char(string="Título", required=True)
    descripcion = fields.Text(string="Descripción")
    anio = fields.Integer(string="Año")
    duracion = fields.Integer(string="Duración")
    disponible = fields.Boolean(string="Disponible", default=True)

    imagen = fields.Image(
        string="Imagen",
        max_width=256,
        max_height=256
    )

    # Relaciones a tablas
    categoria_id = fields.Many2one(
        'videoclub.categoria'
    )

    actor_ids = fields.Many2many(
        'videoclub.actor'
    )