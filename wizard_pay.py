
from openerp import fields, models,api

class PayWedding(models.TransientModel):
    _name = "pay.wedding.wizard"
    
    data analyst job description
    amount = fields.Float()
    
    @api.multi
    def pay(self):
        print self.amount
        print self.env.context
        Model = self.env[self.env.context['active_model']]
        record = Model.browse(self.env.context['active_id'])
        print record.wedding_budget
        if self.amount < record.wedding_budget:
            print "{name} has to give more money".format(name=record.party_name)
        
        
        print record.religion
        result_ids = Model.search([('religion', '=', record.religion)])
        print result_ids
        result_ids = [x.id for x in result_ids]
        '''
        temp = []
        for x in result_ids:
            temp.append(x.id)
        result_ids = temp
            
        '''
        print result_ids
        
        
        
        return {
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'wedding.registration',
            'type': 'ir.actions.act_window',
            'res_id': result_ids,
            'domain': [('id', 'in', result_ids)],
        }
