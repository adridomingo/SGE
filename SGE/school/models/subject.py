from odoo import models, fields, api
class subject(models.Model):
    _name = 'school.subject'
    _description = 'Describe la clase subject'

    name = fields.Char()
    description = fields.Char()
    note_ids = fields.One2many('school.note', 'subject_id')
    teacher_id = fields.Many2one('school.teacher')
    course_id = fields.Many2one('school.course')
    level_course = fields.Selection(related='course_id.level')
    