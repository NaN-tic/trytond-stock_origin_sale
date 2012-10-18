#This file is part stock_origin_sale module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool
from .shipment import *
from .sale import *


def register():
    Pool.register(
        Sale,
        ShipmentOut,
        module='stock_origin_sale', type_='model')
