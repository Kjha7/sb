# -*- coding: utf-8 -*-

from monte_carlo import patterns, stock_patterns

if __name__ == "__main__":
	patterns = patterns.Patterns('data/dataset.csv')
	patterns.ler_dataset()

	x = list(patterns.data.stock.unique())

	print 'Lista de ações no mercado: '
	for acao in x:
		print acao

	a = raw_input('Digite o nome da ação que deseja consultar: ')

	if a.upper() in x:
		stock = stock_patterns.Stock(a.upper(), 'data/dataset.csv')
	else:
		print 'Ação não disponível no mercado'
