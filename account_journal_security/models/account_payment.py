# -*- coding: utf-8 -*-
# DooIT
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, api, SUPERUSER_ID, _

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def _get_to_pay_move_lines_domain(self):

        res = super(AccountPayment, self)._get_to_pay_move_lines_domain()
        
        extended_domain = self.env.user.get_journal_security_domain()

        res.extend(extended_domain)
            
        return res






