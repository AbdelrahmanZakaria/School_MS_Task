from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = 'student.student'
    _description = "This Model To Manage Student's In School"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']

    name = fields.Char(required=True, copy=False)
    age = fields.Integer(tracking=True)
    birth_date = fields.Date()
    note = fields.Text()
    state = fields.Selection(
        [('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancel')],
        default='draft')
    gender = fields.Selection(
        [('m', 'Male'), ('f', 'Female')])
    active = fields.Boolean(default=True)

    @api.constrains('age')
    def Check_Age(self):
        for record in self:
            if record.age < 7 or record.age > 15:
                raise ValidationError(
                    'The Age Of Student Must Be Equal Or Greater Than 7 And Equal Or Less Than 15 Years.')

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'The Name Must Be Unique !')
    ]

    def Draft(self):
        self.state = 'draft'

    def Done(self):
        self.state = 'done'

    def Cancel(self):
        self.state = 'cancel'

    def Return_To_Draft(self):
        if self.state == 'cancel':
            self.state = 'draft'
