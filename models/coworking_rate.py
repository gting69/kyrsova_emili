from odoo import models, fields


class CoworkingRate(models.Model):
    """Модель для визначення вартості оренди"""
    _name = 'coworking.rate'
    _description = 'Coworking Rate'

    name = fields.Char('Rate Name', required=True)
    price = fields.Float('Price per Hour', required=True)
    currency_id = fields.Many2one(
        'res.currency',
        'Currency',
        default=lambda self: self.env.company.currency_id
    )
