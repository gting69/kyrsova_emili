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
    manager_id = fields.Many2one('res.users', domain=[('share', '=', False)])
    start_date = fields.Datetime(required=True)
    end_date = fields.Datetime(required=True)

    rate_id = fields.Many2one('coworking.rate')
    total_amount = fields.Float(compute='_compute_total_amount', store=True)
    bonus_earned = fields.Float(compute='_compute_bonus', store=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], default='draft', tracking=True)

    @api.depends('start_date', 'end_date', 'rate_id')
    def _compute_total_amount(self):
        for record in self:
            if record.start_date and record.end_date and record.rate_id:
                diff = record.end_date - record.start_date
                duration = diff.total_seconds() / 3600
                record.total_amount = duration * record.rate_id.price
            else:
                record.total_amount = 0.0

    @api.depends('total_amount')
    def _compute_bonus(self):
        for record in self:
            record.bonus_earned = record.total_amount * 0.05

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            seq = self.env['ir.sequence']
            vals['name'] = seq.next_by_code('coworking.booking') or 'New'
        return super().create(vals)

    def action_confirm(self):
        self.state = 'confirmed'
