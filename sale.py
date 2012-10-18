#This file is part stock_origin_purchase module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['Sale']
__metaclass__ = PoolMeta

class Sale:
    'Sale'
    __name__ = 'sale.sale'

    def create_shipment(self, shipment_type):
        shipments = super(Sale, self).create_shipment(shipment_type)
        if shipment_type == 'out':
            Shipment = Pool().get('stock.shipment.out')
        elif shipment_type == 'return':
            Shipment = Pool().get('stock.shipment.out.return')
        else:
            return None

        if shipments:
            for shipment in shipments:
                values = {
                    'origin': 'sale.sale,%s' % (self.id),
                }
                Shipment.write([shipment], values)
        return shipments

