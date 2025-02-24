# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields, _

class Users(models.Model):
    _inherit = 'res.users'

    def get_journal_security_domain(self):
        
        journal_security_domain = [
                                    '|','|',
                                    ('journal_id.modification_user_ids', 'ilike',self.env.user.id),
                                    ('journal_id.user_ids', 'ilike', self.env.user.id),
                                    '&',
                                    ('journal_id.modification_user_ids', '=', False),
                                    ('journal_id.user_ids', '=', False),
                                ]
        
        return journal_security_domain