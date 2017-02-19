# -*- coding: utf-8 -*-

from patterns import Patterns
from stock_patterns import Stock

stock = Stock('A', 'data/dataset.csv')
stock.read_dataset()
stock.get_stock_patterns()

stock.compare_with_previous()