from openerp import fields, models,api

class PayCash(models.TransientModel):
    _name = "pay.cash"
    
    payment_type = fields.Char(default=lambda self: self._get_default_name(), readonly=True) 
    party_name = fields.Char(required=True)
    amount = fields.Float(required=True)
    date = fields.Date(required=True)
    
    @api.model
    def _get_default_name(self):
        print self.env.context
        Model = self.env[self.env.context['active_model']] # get active model i.e pay.method()
        record = Model.browse(self.env.context['active_id'])
        return record.payment_type
        #self.payment_description = record.payment_type
    
    @api.multi
    def proceed(self):
        print "Hello"
        
