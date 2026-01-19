from odoo import models, fields


class CoworkingDesk(models.Model):
    """Модель для обліку конкретних робочих місць (столів)"""
    _name = 'coworking.desk'
    _description = 'Coworking Desk'

    name = fields.Char(string='Desk Number', required=True)
    room_id = fields.Many2one('coworking.room', string='Room', required=True)
    is_premium = fields.Boolean(string='Premium Desk', default=False)
    active = fields.Boolean(default=True)
