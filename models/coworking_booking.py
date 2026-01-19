from odoo import models, fields, api


class CoworkingBooking(models.Model):
    """Основна модель для реєстрації бронювань"""
    _name = 'coworking.booking'
    _description = 'Booking'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, copy=False, readonly=True, default='New')
    partner_id = fields.Many2one('res.partner', required=True)
    room_id = fields.Many2one('coworking.room')
    desk_id = fields.Many2one('coworking.desk')
    rate_id = fields.Many2one('coworking.rate')
    start_date = fields.Datetime(required=True)
    end_date = fields.Datetime(required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], default='draft', tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            seq_code = 'coworking.booking'
            next_name = self.env['ir.sequence'].next_by_code(seq_code)
            vals['name'] = next_name or 'New'
        return super(CoworkingBooking, self).create(vals)

    def action_confirm(self):
        self.state = 'confirmed'
