from odoo import models, fields

class cliente(models.Model):
    _name = 'videoclub.cliente'
    _description = 'Describe la clase cliente'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Nombre", required=True)
    telefono = fields.Char(string="Teléfono")
    email = fields.Char(string="Email")

    alquiler_ids = fields.One2many(
        'videoclub.alquiler',
        'cliente_id'
    )