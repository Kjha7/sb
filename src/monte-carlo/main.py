# -*- coding: utf-8 -*-

from patterns import Patterns
from stock_patterns import Stock

if __name__ == "__main__":
	patterns = Patterns('data/dataset.csv')
	patterns.ler_dataset()

	x = list(patterns.data.stock.unique())

	print 'Lista de ações no mercado: '
	for acao in x:
		print acao

	a = raw_input('Digite o nome da ação que deseja consultar: ')

	if a.upper() in x:
		stock = Stock(a.upper(), 'data/dataset.csv')
	else:
		print 'Ação não disponível no mercado'