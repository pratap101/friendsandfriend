# -*- coding: utf-8 -*-

from openerp import fields, models

class Farming(models.Model):
    _name = 'farming.details'
    
    crop_name = fields.Char()
    start_date = fields.Date()
    end_date = fields.Date()
    land = fields.Char()
    person_name = fields.Char()
    land_info = fields.One2many(
         'agriculture.details',
         'land_name',
         'Land Info')
                                 
