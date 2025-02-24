from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
 
    use_default_vendor_template = fields.Many2one('mail.template',
        string='Usar plantilla por defecto (Proveedores)',
        config_parameter='account.use_default_vendor_template',
        domain = [('model_id', '=', 'account.payment')]
    )
    use_default_customer_template = fields.Many2one('mail.template',
        string='Usar plantilla por defecto (Clientes)',
        config_parameter='account.use_default_customer_template',
        domain = [('model_id', '=', 'account.payment')]
    )