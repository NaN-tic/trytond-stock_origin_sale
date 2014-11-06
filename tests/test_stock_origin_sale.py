#!/usr/bin/env python
# This file is part stock_origin_sale_sale module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_depends


class StockOriginSaleTestCase(unittest.TestCase):
    'Test Stock Origin Sale module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('stock_origin_sale')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockOriginSaleTestCase))
    return suite
