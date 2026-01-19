from odoo import models, fields


class QuickBookingWizard(models.TransientModel):
    _name = 'quick.booking.wizard'
    _description = 'Quick Booking Wizard'

    partner_id = fields.Many2one('res.partner', required=True)
    room_id = fields.Many2one('coworking.room', required=True)
    start_date = fields.Datetime(default=fields.Datetime.now)

    def action_create_booking(self):
        self.env['coworking.booking'].create({
            'partner_id': self.partner_id.id,
            'room_id': self.room_id.id,
            'start_date': self.start_date,
            'end_date': fields.Datetime.now(),
        })
