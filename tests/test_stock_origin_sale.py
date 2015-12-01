# This file is part of the stock_origin_sale module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockOriginSaleTestCase(ModuleTestCase):
    'Test Stock Origin Sale module'
    module = 'stock_origin_sale'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockOriginSaleTestCase))
    return suite