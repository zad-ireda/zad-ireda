from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    res_user_phone = fields.Char(related='partner_id.phone', string='phone'readonly=True)
    
    res_user_mobile =  fields.Char(related='partner_id.mobile', string='mobile' readonly=True)
