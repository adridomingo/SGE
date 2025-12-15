from odoo import models, fields, api
class paciente(models.Model):
    _name='hospital.paciente'
    _description= 'describe la clase paciente'

    name = fields.Char()
    surname = fields.Char()
    direccion = fields.Char()
    poblacion = fields.Char()
    provincia = fields.Char()
    postal = fields.Integer()
    birthday = fields.Date()
    telefono = fields.Integer()

    medico_id = fields.Many2one('hospital.medico')
    ingreso_id = fields.One2many(
        'hospital.ingreso',
        'paciente_id'
    )

    diagnostico_id = fields.One2many(
        'hospital.diagnostico',
        'paciente_id'
    )
