# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
	#_name = 'product.template'
    _inherit = 'product.template'

    ppartno = fields.Char('OE Number')
    mpartno = fields.Char('Vendor Number')
    default_code = fields.Char('Brand')
