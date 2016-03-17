from openerp import fields, models,api
from openerp.osv import osv


class PayCheque(models.TransientModel):
    _name = "pay.cheque"
    
    payment_type = fields.Char(default=lambda self: self._get_default_name(),  readonly=True)
    party_name = fields.Char(required=True)
    bank = fields.Char(required=True)
    date = fields.Date(required=True)
    cheque_number = fields.Integer(required=True)
    amount = fields.Float(required=True)
    
    
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
        print self.env.context
        Model = self.env[self.env.context['active_model']] # get active model i.e pay.method()
        print Model
        
        record = Model.browse(self.env.context['active_id'])
        print record
        print record.payment_type
        self.payment_type = record.payment_type
        raise osv.except_osv(('No Customer Defined!'), ('Before choosing a product,\n select a customer in the sales form.'))
