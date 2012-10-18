#This file is part stock_origin_sale module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['ShipmentOut']
__metaclass__ = PoolMeta

class ShipmentOut:
    "Customer Shipment"
    __name__ = 'stock.shipment.out'

    @classmethod
    def _get_origin(cls):
        return super(ShipmentOut, cls)._get_origin() + ['sale.sale']
