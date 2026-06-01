from odoo import models, fields

class incidencia(models.Model):
    _name = 'videoclub.incidencia'
    _description = 'Describe la clase incidencia'

    name = fields.Char(string="Descripción", required=True)
    fecha = fields.Date(string="Fecha", default=fields.Date.today)
    gravedad = fields.Selection(
        [
            ('baja', 'Baja'),
            ('media', 'Media'),
            ('alta', 'Alta')
        ],
        string="Gravedad",
        default='baja'
    )
    resuelta = fields.Boolean(string="Resuelta", default=False)

    alquiler_id = fields.Many2one(
        'videoclub.alquiler',
        string="Alquiler"
    )