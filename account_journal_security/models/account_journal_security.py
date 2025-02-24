# -*- coding: utf-8 -*-
# DooIT
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    def action_open_reconcile(self):

        res = super(AccountJournal, self).action_open_reconcile()
        
        extended_domain = self.env.user.get_journal_security_domain()

        res['domain'].extend(extended_domain)
        
        return res