
from openerp import fields, models,api
#from cash import PayCash

class pay(models.Model):

    _name = 'pay.method'
    
    payment_type = fields.Selection([
        ('cash','Cash'),
        ('cheque','Cheque')
    ])
    
    @api.multi
    def pay(self):
        
        #if ' ' in self.payment_type:
            #return "Please select available option"
               
        if 'cash' in self.payment_type:
             return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'pay.cash',
            'type': 'ir.actions.act_window',
            'target':'new'
            #'res_id': result_ids,
            #'domain': [('id', 'in', result_ids)],
            }
            
        if 'cheque' in self.payment_type:
            return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'pay.cheque',
            'type': 'ir.actions.act_window',
            'target':'new'
            #'res_id': result_ids,
            #'domain': [('id', 'in', result_ids)],
            }
