from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class ingreso(models.Model):
    _name='hospital.ingreso'
    _description= 'describe la clase ingreso'

    habitacion = fields.Integer()
    cama = fields.Selection(
    [('1', 'Cama 1'), ('2', 'Cama 2')],
    string="Cama",
    required=True
    )
    fechaIngreso = fields.Date(default=fields.Date.today)
    fechaAlta = fields.Date()
    sintomas = fields.Char()
    active = fields.Boolean(default=True)
    diasIngresado = fields.Integer(compute="_dias_ingresado")

    medico_id = fields.Many2one('hospital.medico')
    paciente_id = fields.Many2one('hospital.paciente')
    diagnostico_id = fields.One2many(
        'hospital.diagnostico',
        'ingreso_id'
    )

    @api.constrains('fechaIngreso')
    def _check_fecha_ingreso(self):
        for record in self:
            if record.fechaIngreso:
                if record.fechaIngreso < fields.Date.today() - timedelta(days=7):
                    raise ValidationError(
                        "La fecha de ingreso no puede ser anterior a una semana."
                    )
    
    @api.constrains('fechaAlta')
    def _check_fecha_alta(self):
        for record in self:
            if record.fechaAlta and record.fechaAlta > fields.Date.today():
                raise ValidationError(
                    "La fecha de alta no puede ser posterior a hoy."
                )
            
    @api.depends('fechaIngreso', 'fechaAlta')
    def _dias_ingresado(self):
        for record in self:
            end_date = record.fechaAlta or fields.Date.today()
            if record.fechaIngreso:
                record.diasIngresado = (end_date - record.fechaIngreso).days
            else:
                record.diasIngresado = 0

    @api.constrains('habitacion', 'cama')
    def _no_repetir_num(self):
        for record in self:
            domain = [
                ('habitacion', '=', record.habitacion),
                ('cama', '=', record.cama),
                ('id', '!=', record.id),
                ('active', '=', True),
            ]
            if self.search_count(domain):
                raise ValidationError(
                    "Esa cama ya está ocupada en esa habitación."
                )