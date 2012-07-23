#This file is part stock_origin_sale module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pool import Pool

class ShipmentOut(ModelSQL, ModelView):
    _name = 'stock.shipment.out'

    def origin_get(self):
        res = super(ShipmentOut, self).origin_get()
        model_obj = Pool().get('ir.model')
        model_ids = model_obj.search([
            ('model', '=', 'sale.sale'),
            ])
        for model in model_obj.browse(model_ids):
            res.append([model.model, model.name])
        return res

ShipmentOut()
