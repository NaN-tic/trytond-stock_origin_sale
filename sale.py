#This file is part stock_origin_purchase module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.transaction import Transaction
from trytond.pool import Pool

class Sale(ModelSQL, ModelView):
    _name = 'sale.sale'

    def create_shipment(self, sale, shipment_type):
        shipments = super(Sale, self).create_shipment(sale, shipment_type)
        if shipment_type == 'out':
            shipment_obj = Pool().get('stock.shipment.out')
        elif shipment_type == 'return':
            shipment_obj = Pool().get('stock.shipment.out.return')
        else:
            return None

        if shipments:
            for shipment in shipments:
                values = {
                    'origin': 'sale.sale,%s' % (sale.id),
                }
                shipment_id = shipment_obj.write([shipment], values)

Sale()
