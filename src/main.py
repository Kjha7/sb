# -*- coding: utf-8 -*-

import matplotlib, csv

with open('data/padrao.txt') as arquivo:
    titulo = arquivo.read().split(', ')

reader = csv.reader(open('data/dataset.csv', 'rb'))

filtro = open('data/result.txt', 'w')

for linha in reader:
    l = list(linha)
    if(l[1] == 'AA'):
        filtro.write(' '.join(l) + '\n')
    
filtro.close()