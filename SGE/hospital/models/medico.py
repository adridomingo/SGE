from odoo import models, fields, api
class medico(models.Model):
    _name='hospital.medico'
    _description= 'describe la clase medico'

    name = fields.Char()
    surname = fields.Char()
    telefono = fields.Integer()
    especialidad = fields.Char()
    numero = fields.Integer()
    image = fields.Image()

    _sql_constraints = [
    ('numero_unique',
     'unique(numero)',
     'El número de colegiado debe ser único.')
    ]

    paciente_id = fields.One2many('hospital.paciente', 'medico_id')
    ingreso_id = fields.One2many(
        'hospital.ingreso',
        'medico_id'
    )

    diagnostico_id = fields.One2many(
        'hospital.diagnostico',
        'medico_id'
    )