from odoo import fields, models, _, api
from odoo.exceptions import UserError, ValidationError


class AccountMove(models.Model):
    _inherit = 'account.move'

    def open_credit_notes_report(self):
        return self.env.ref('credit_notes_report.credit_notes_report_action').report_action(self)
