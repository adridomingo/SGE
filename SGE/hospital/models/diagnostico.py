from odoo import models, fields, api
class diagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'Diagnóstico médico'

    diagnostico = fields.Char()
    fecha = fields.Date(default=fields.Date.today)

    ingreso_id = fields.Many2one('hospital.ingreso')
    medico_id = fields.Many2one('hospital.medico')
    paciente_id = fields.Many2one('hospital.paciente')