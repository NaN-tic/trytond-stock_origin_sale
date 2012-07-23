#This file is part stock_origin_sale module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
{
    'name': 'Stock Origin Sale',
    'name_ca_ES': 'Origen estoc de comanda de compra',
    'name_es_ES': 'Origen stock de pedido de venta',
    'version': '2.4.0',
    'author': 'Zikzakmedia',
    'email': 'zikzak@zikzakmedia.com',
    'website': 'http://www.zikzakmedia.com/',
    'description': '''Add origin of shipment: Sale''',
    'description_ca_ES': '''Afegeix l'origen del albarà: comanda de venda''',
    'description_es_ES': '''Añade el origen del albarán: pedido de venta''',
    'depends': [
        'ir',
        'res',
        'stock',
        'stock_origin',
        'sale',
    ],
    'xml': [
    ],
    'translation': [
    ]
}
