# -*- coding: utf-8 -*-
from odoo import models, fields, api
#Definimos el modelo de datos
class lista_tareas(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'
    #Elementos de cada fila del modelo de datos 
    #Los tipos de datos a usar en el ORM son
    #https://www.odoo.com/documentation/18.0/developer/reference/addons/orm.html#fields

    task = fields.Char(string= 'Tarea', help='Nombre de la tarea')
    prioridad = fields.Integer(default=8)
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()
    responsable = fields.Many2one('lista_tareas.responsable')

    _sql_constraints = [
        ('prioridad_positiva', 'check(prioridad>0)', 'La prioridad tiene que ser positiva')
    ]

    #Este computo depende de la variable prioridad
    @api.depends('prioridad')
    #Funcion para calcular el valor de urgente
    def _value_urgente(self):
    #Para cada registro
        for tarea in self:
        #Si la prioridad es mayor que 10, se considera urgente, en otro caso no lo es
            if tarea.prioridad>10:
                tarea.urgente = True
            else:
                tarea.urgente = False

class responsable(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'lista_tareas.responsable'
    _description = 'Informacion del responsable'

    name = fields.Char()
    dni = fields.Char()
    task_id=fields.One2many('lista_tareas.lista_tareas', 'responsable')

    _sql_constraints = [
        ('dni_uniq', 'unique(dni)', 'El dni tiene que ser unico')
    ]
