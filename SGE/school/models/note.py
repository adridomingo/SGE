from odoo import models, fields, api


class note(models.Model):
    _name='school.note'
    _description= 'describe la clase notas'

    note = fields.Integer()

    subject_id = fields.Many2one('school.subject')
    student_id = fields.Many2one('school.student')

    _sql_constraints = [
        ('nota_unica_alumno_asig', 
         'unique( subject_id, student_id)',
         'El alumno solo puede tener una nota por asignatura' ),
    ]