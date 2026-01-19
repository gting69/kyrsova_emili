from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_coworking_client = fields.Boolean(default=False)
    booking_ids = fields.One2many('coworking.booking', 'partner_id')


class ResUsers(models.Model):
    _inherit = 'res.users'

    is_coworking_manager = fields.Boolean(default=False)
