# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime

import secrets
import string


class school(models.Model):
    _name = 'school.student'
    _description = 'Describe la clase student'

    name = fields.Char()
    surname = fields.Char()
    birthday = fields.Date()
    age = fields.Integer(compute='_age_calculate')
    gender = fields.Selection([
        ('1', 'Femenino'),
        ('2', 'Masculino')
    ])
    note_ids = fields.One2many('school.note', 'student_id')
    country_id = fields.Many2one('res.country', default=lambda self : self.env.ref('base.es'))
    province = fields.Many2one('res.country.state', domain="[('country_id', '=', country_id)]")
    password = fields.Char()
    level = fields.Char()
    dni = fields.Char()
    course_id = fields.Many2one('school.course')

    image=fields.Image(max_width=200, max_height=200)
    state = fields.Selection([
        ('1', 'Prematriculado'),
        ('2', 'Matriculado'),
        ('3', 'Ex-alumno')
    ])

    _sql_constraints = [
        ('dni_unico', 'unique(dni)', 'El dni debe ser unico')
    ]

    def regenerar(self):
        for student in self:
            alphabet = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(alphabet) for i in range(12))
            student.password=password

    @api.depends('birthday')
    def _age_calculate(self):
        today = fields.Date.today()
        for student in self:
            if student.birthday:
                student.age = relativedelta(today, student.birthday).years
            else:
                student.age=0
