# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date 

class Register(models.Model):
    _inherit = ['mail.thread']
    _name = 'warranty.register'
    _description = 'Register warranty type'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    warranty_type = fields.Selection([('type 1','Check'),
                            ('type 2','Promissory Note'),
                            ('type 3','Bank Guarantee')],
                             string='Warranty Type', default='Check')

    warranty_state = fields.Selection([('state 1','Preparing'),
                                          ('state 2','Active'),
                                         ('state 3','Expired'),
                                         ('state 4', 'Refunded')],
                                   string='Warranty State', default='Preparing',
                                   track_visibility=True)


    date_start = fields.Date(string='Warranty Since:')
    date_end = fields.Date(string='Warranty Until:')
    date_warning = fields.Date(string="Warning Date", store=True,
        compute='_expiration_warning')


    customer = fields.Many2one('res.partner',
        ondelete='cascade', string="Customer", required=False)

    provider = fields.Many2one('res.user',
        ondelete='cascade', string="Provider", required=False)

    release = fields.Boolean(string='Release State', default=False)

    

    def _track_subtype(self, init_values):
        if 'warranty_state' in init_values:
            self.message_post(body="State changed!", subject="State information",
                             subtype="mt_note", partner_ids=self.customer )
        return False
    

    @api.onchange('date_end', 'customer')
    def _expiration_warning(self):
        for r in self:
            if r.date_end == date.today():
                r.date_warning = date.today()
                r.message_post(
                    body="Today warranty is going to be expired",
                    subject="State information",
                    subtype="mt_note", 
                    partner_ids=r.customer)

            else:
                r.date_warning = r.date_end






class State(models.Model):
    _name = 'warranty.state'
    _description = 'Defining Warranty State by Users'

    state_name = fields.Char(string="State", required=True)
    description = fields.Text()