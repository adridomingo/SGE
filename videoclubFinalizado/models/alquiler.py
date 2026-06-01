from odoo import models, fields, api
from odoo.exceptions import ValidationError

class alquiler(models.Model):
    _name = 'videoclub.alquiler'
    _description = 'Describe la clase alquiler'

    fecha_alquiler = fields.Date(default=fields.Date.today)
    fecha_devolucion = fields.Date(string="Fecha de devolución")

    # Campo selection
    estado = fields.Selection(
        [
            ('alquilado', 'Alquilado'),
            ('devuelto', 'Devuelto')
        ],
        string="Estado",
        default='alquilado'
    )

    # Campo related
    cliente_email = fields.Char(
        related='cliente_id.email',
        string="Email del cliente",
        store=True
    )
    # Campo con reference
    documento_ref = fields.Reference(
        selection=[
            ('videoclub.pelicula', 'Película'),
            ('videoclub.cliente', 'Cliente')
        ],
        string="Referencia"
    )

    # Campo calculado
    dias_alquiler = fields.Integer(
        string="Días de alquiler",
        compute="_calcular_dias",
        aggregator="avg"
    )

    contador = fields.Integer(
        string="Alquileres",
        default=1,
        store=True
    )
    
    # Relaciones a tablas
    cliente_id = fields.Many2one(
        'videoclub.cliente'
    )

    pelicula_id = fields.Many2one(
        'videoclub.pelicula'
    )

    incidencia_ids = fields.One2many(
        'videoclub.incidencia',
        'alquiler_id',
        string="Incidencias"
    )

    # Funcion para el formulario que marca como devuelto
    def action_devolver(self):
        for record in self:
            record.estado = 'devuelto'
            if not record.fecha_devolucion:
                record.fecha_devolucion = fields.Date.today()

    # Funcion para el formulario que reabre alquiler, no esta devuelto
    def action_reabrir(self):
        for record in self:
            record.estado = 'alquilado'
            record.fecha_devolucion = False


    # Funcion que comprueba que la fecha de devolucion sea mayor que la fecha de alquiler
    @api.constrains('fecha_alquiler', 'fecha_devolucion')
    def _check_fechas(self):
        for record in self:
            if record.fecha_devolucion and record.fecha_devolucion < record.fecha_alquiler:
                raise ValidationError("La fecha de devolución no puede ser anterior al alquiler.")
    
    # Funcion que calcula los dias que ha habido entre la fecha de alquiler y la de devolución
    @api.depends('fecha_alquiler', 'fecha_devolucion')
    def _calcular_dias(self):
        for record in self:
            if record.fecha_devolucion and record.fecha_alquiler:
                record.dias_alquiler = (record.fecha_devolucion - record.fecha_alquiler).days
            else:
                record.dias_alquiler = 0