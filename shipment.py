#This file is part stock_origin_sale module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta

__all__ = ['ShipmentOut', 'ShipmentOutReturn']
__metaclass__ = PoolMeta


class ShipmentOut:
    __name__ = 'stock.shipment.out'

    @classmethod
    def get_origin_value(cls, shipments, name):
        SaleLine = Pool().get('sale.line')
        origin = super(ShipmentOut, cls).get_origin_value(shipments, name)
        for shipment in shipments:
            for m in shipment.outgoing_moves:
                if m.origin and isinstance(m.origin, SaleLine):
                    origin[shipment.id] = 'sale.sale,%s' % (m.origin.sale.id)
                    break
        return origin

    @classmethod
    def _get_origin(cls):
        return super(ShipmentOut, cls)._get_origin() + ['sale.sale']


class ShipmentOutReturn:
    __name__ = 'stock.shipment.out.return'

    @classmethod
    def get_origin_value(cls, shipments, name):
        SaleLine = Pool().get('sale.line')
        origin = super(ShipmentOutReturn, cls).get_origin_value(shipments, name)
        for shipment in shipments:
            for m in shipment.incoming_moves:
                if m.origin and isinstance(m.origin, SaleLine):
                    origin[shipment.id] = 'sale.sale,%s' % (m.origin.sale.id)
                    break
        return origin

    @classmethod
    def _get_origin(cls):
        return super(ShipmentOutReturn, cls)._get_origin() + ['sale.sale']
