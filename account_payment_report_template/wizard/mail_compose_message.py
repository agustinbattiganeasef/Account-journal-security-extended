from odoo import models, fields, api

class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.onchange('composition_mode')
    def _onchange_template_id(self):
        use_default_customer_template = self.env['ir.config_parameter'].sudo().get_param('account.use_default_customer_template', default=False)
        use_default_vendor_template = self.env['ir.config_parameter'].sudo().get_param('account.use_default_vendor_template', default=False)

        if self.env.context.get('active_id'):
            payment = self.env['account.payment'].browse(self.env.context['active_id'])

            if payment.payment_type == 'inbound' and use_default_customer_template:
                template = self.env['mail.template'].search([('id', '=', use_default_customer_template)])
            elif payment.payment_type == 'outbound' and use_default_vendor_template:
                template = self.env['mail.template'].search([('id', '=', use_default_vendor_template)])
            else:
                template = False

            if template:
                self.template_id = template.id


