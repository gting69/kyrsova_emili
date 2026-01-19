from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_coworking_client = fields.Boolean(default=False)
    booking_ids = fields.One2many('coworking.booking', 'partner_id')
    total_bonuses = fields.Float(compute='_compute_total_bonuses')

    @api.depends('booking_ids.bonus_earned', 'booking_ids.state')
    def _compute_total_bonuses(self):
        for partner in self:
            confirmed_bookings = partner.booking_ids.filtered(
                lambda b: b.state == 'confirmed'
            )
            partner.total_bonuses = sum(
                confirmed_bookings.mapped('bonus_earned')
            )


class ResUsers(models.Model):
    _inherit = 'res.users'

    is_coworking_manager = fields.Boolean(default=False)
