# -*- coding: utf-8 -*-

from openerp import fields, models

class LandDetail(models.Model):
    _name = 'agriculture.details'
    
    area = fields.Float()
    length = fields.Float()
    width = fields.Float()
    type_of_soil = fields.Selection([
        ('alluvial_soil','Alluvial soil'),
        ('red_soil','Red soil'),
        ('black_soil',' Black soil'),
        ('desert_soil','Desert soil')
    ])
    geographical_area = fields.Float()
    land_name = fields.Many2one('farming.details','Land Name')
    land_person = fields.Many2many(
        'farming.details',
        'land_person_information',
        'land_info',
        'person_info',
        'Land Person')
    code = fields.Char()                                
 
