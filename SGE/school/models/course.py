from odoo import models, fields, api
class course(models.Model):
    _name='school.course'
    _description= 'describe la clase course'

    name = fields.Char()
    level = fields.Selection([
        {'1', 'Primero'},
        {'2', 'Segundo'}
    ])
    subject_id = fields.One2many('school.subject', 'course_id')
    student_ids = fields.One2many('school.student', 'course_id')
