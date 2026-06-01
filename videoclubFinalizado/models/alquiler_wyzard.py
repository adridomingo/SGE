from odoo import models, fields, api

# Modelo auxiliar para líneas de incidencia
class IncidenciaAux(models.TransientModel):
    _name = 'videoclub.incidencia_aux'
    _description = 'Modelo auxiliar de incidencia'

    name_aux        = fields.Char(string='Descripción')
    gravedad_aux    = fields.Selection([
        ('baja',  'Baja'),
        ('media', 'Media'),
        ('alta',  'Alta')
    ], string='Gravedad', default='baja')
    alquiler_id_aux = fields.Many2one('videoclub.alquiler_aux', string='Alquiler')


# Modelo auxiliar principal
class AlquilerAux(models.TransientModel):
    _name = 'videoclub.alquiler_aux'
    _description = 'Modelo auxiliar de alquiler'

    # Estado del wizard
    state_wizard = fields.Selection([
        ('1', 'Cliente'),
        ('2', 'Película'),
        ('3', 'Incidencias'),
        ('4', 'Confirmar'),
    ], default='1', string='Etapa')

    # Etapa 1: Cliente
    crear_cliente_aux   = fields.Boolean(string='Crear cliente nuevo')
    cliente_id_aux      = fields.Many2one('videoclub.cliente', string='Cliente',
                                          domain="[('email', '!=', False)]")
    name_cliente_aux    = fields.Char(string='Nombre del cliente')
    email_cliente_aux   = fields.Char(string='Email')
    telefono_cliente_aux= fields.Char(string='Teléfono')

    # Etapa 2: Película
    pelicula_id_aux     = fields.Many2one('videoclub.pelicula', string='Película',
                                          domain="[('disponible', '=', True)]")
    categoria_aux       = fields.Char(related='pelicula_id_aux.categoria_id.name',
                                      string='Categoría')
    anio_aux            = fields.Integer(related='pelicula_id_aux.anio', string='Año')
    duracion_aux        = fields.Integer(related='pelicula_id_aux.duracion', string='Duración')

    # Etapa 3: Incidencias
    name_incidencia_aux     = fields.Char(string='Descripción incidencia')
    gravedad_incidencia_aux = fields.Selection([
        ('baja',  'Baja'),
        ('media', 'Media'),
        ('alta',  'Alta')
    ], string='Gravedad', default='baja')
    incidencia_id_aux = fields.One2many('videoclub.incidencia_aux', 'alquiler_id_aux',
                                        string='Incidencias')

    # Etapa 4: Confirmación
    fecha_alquiler_aux   = fields.Date(string='Fecha de alquiler', default=fields.Date.today)
    fecha_devolucion_aux = fields.Date(string='Fecha de devolución prevista')

    # Navegación
    def next(self):
        if self.state_wizard == '1':
            self.state_wizard = '2'
        elif self.state_wizard == '2':
            self.state_wizard = '3'
        elif self.state_wizard == '3':
            self.state_wizard = '4'
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

    def previous(self):
        if self.state_wizard == '2':
            self.state_wizard = '1'
        elif self.state_wizard == '3':
            self.state_wizard = '2'
        elif self.state_wizard == '4':
            self.state_wizard = '3'
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

    # Añadir incidencia a la lista
    def add_incidencia(self):
        for rec in self:
            rec.write({'incidencia_id_aux': [(0, 0, {
                'name_aux':     rec.name_incidencia_aux,
                'gravedad_aux': rec.gravedad_incidencia_aux,
            })]})
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

    # Crear registros reales
    def create_alquiler(self):
        for rec in self:

            # Crear cliente si es nuevo
            if rec.crear_cliente_aux:
                cliente = rec.env['videoclub.cliente'].create({
                    'name':     rec.name_cliente_aux,
                    'email':    rec.email_cliente_aux,
                    'telefono': rec.telefono_cliente_aux,
                })
            else:
                cliente = rec.cliente_id_aux

            # Marcar película como no disponible
            rec.pelicula_id_aux.disponible = False

            # Crear el alquiler
            alquiler = rec.env['videoclub.alquiler'].create({
                'cliente_id':       cliente.id,
                'pelicula_id':      rec.pelicula_id_aux.id,
                'fecha_alquiler':   rec.fecha_alquiler_aux,
                'fecha_devolucion': rec.fecha_devolucion_aux,
                'estado':           'alquilado',
            })

            # Crear incidencias enlazadas al alquiler
            for inc in rec.incidencia_id_aux:
                rec.env['videoclub.incidencia'].create({
                    'name':        inc.name_aux,
                    'gravedad':    inc.gravedad_aux,
                    'alquiler_id': alquiler.id,
                })

        return {
            'type': 'ir.actions.act_window_close',
        }