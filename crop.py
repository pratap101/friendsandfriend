# -*- coding: utf-8 -*-

from openerp import fields, models, api
import psycopg2
from openerp import tools
#import odoorpc

class CropDetail(models.Model):
    _name = 'crop.details'
    
    name = fields.Char()
    crop_type = fields.Selection([
               ('kharif','Kharif'),
               ('rabi','Rabi'),
               ('zaid','Zaid')
               ])
    seeds = fields.Char()
    per_hectare_yield = fields.Float()
    season = fields.Char()

    @api.multi
    def confirm(self):
        print "Pratap Singh"
        print self.name
        print self.crop_type
        print self.seeds
        print self.season
        
        
        
        #partners = self.pool.get('crop.details').browse(cr, uid, ids)
        #print partners
        #p = self.name
        #Env = env(cr,uid,context)
        #recs = self.Env['crop.details']
        #recs = recs.search('name')
        #for rec in recs:
            #print rec.name
        #cprint("Pratap Singh")
        #for record in p:
           #print record
        #conn = psycopg2.connect(database="training", user="odoo", password="odoo", host="127.0.0.1", port="5432")
        #print "Opened database successfully"

        #cur = conn.cursor()

        #cur.execute("SELECT name from crop_details")
        #rows = cur.fetchall()
        #for row in rows:
            #print "Crop Name = ", row[0], "\n"

        #print "Operation done successfully";
        #conn.close()
