from odoo import models, fields


class CoworkingManagerShift(models.Model):
    """Модель для розкладу роботи менеджерів"""
    _name = 'coworking.manager.shift'
    _description = 'Manager Shift'

    manager_id = fields.Many2one(
        'res.users',
        string='Manager',
        domain=[('share', '=', False)],
        required=True
    )
    start_date = fields.Datetime(required=True)
    end_date = fields.Datetime(required=True)
    room_id = fields.Many2one('coworking.room')
