# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Provider(models.Model):
    _inherit = 'res.users'
    _name = 'warranty.provider'
    _description = 'Customer of contraction'

    warranty_ids = fields.One2many(
        'warranty.register', 'customer', string="Registered Warranties")