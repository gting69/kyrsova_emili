from odoo import models, fields


class CoworkingRoom(models.Model):
    """Модель для опису кімнат у коворкінгу"""
    _name = 'coworking.room'
    _description = 'Coworking Room'

    name = fields.Char(required=True)
    capacity = fields.Integer()
    active = fields.Boolean(default=True)
    description = fields.Text()
