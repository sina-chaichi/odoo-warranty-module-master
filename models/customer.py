# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Customer(models.Model):
    _inherit = 'res.partner'
    _name = 'warranty.customer'
    _description = 'Customer of contraction'

    warranty_ids = fields.One2many(
        'warranty.register', 'customer', string="Registered Warranties")