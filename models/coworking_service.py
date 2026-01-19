from odoo import models, fields


class CoworkingService(models.Model):
    """Додаткові послуги: кава, друк, прибирання"""
    _name = 'coworking.service'
    _description = 'Coworking Service'

    name = fields.Char(required=True)
    cost = fields.Float()
