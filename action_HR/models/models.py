# -*- coding: utf-8 -*-
from odoo import models, fields, api


class action_HR(models.Model):
    _inherit = 'hr.employee'

    address_name = fields.Char(string='Address')
    social_number = fields.Integer(string='Social Insurance Number')
    social_amount = fields.Integer(string='Social Insurance Amount')
    social_date = fields.Date(string='Social Insurance Date')
    
