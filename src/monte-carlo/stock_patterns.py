# -*- coding: utf-8 -*-
from patterns import Patterns
from scipy.spatial import distance

class Stock(Patterns):

    def __init__(self, stock, dataset):
        
        super(self.__class__, self).__init__(dataset)
        self._stock = stock
        self._pattern = {}
        self._performances = {}
        self.ler_dataset()
        self.gerar_padroes()
        self.comparar_com_anteriores()

    @property
    def stock(self):
        return self._stock

    @property
    def pattern(self):
        return self._pattern

    @property
    def performances(self):
        return self._performances

    def ler_dataset(self):
        super(Stock, self).ler_dataset()

    def mudanca_percentual(self, ant, pos):
        return super(self.__class__, self).mudanca_percentual(ant, pos)

    def gerar_padroes(self):

        pattern_array = []
        
        x = self.data.index.get_loc(self.data[self.data.stock == self._stock].iloc[0].name) + 10
        y = len(self.data[self.data.stock == self._stock]) - 10

        i = 0

        while i < y:

            pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 10], self.data['avg'][x - 9]))
            pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 9], self.data['avg'][x - 8]))
            pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 8], self.data['avg'][x - 7]))
            pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 7], self.data['avg'][x - 6]))
            pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 6], self.data['avg'][x - 5]))
            pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 5], self.data['avg'][x - 4]))
            pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 4], self.data['avg'][x - 3]))
            pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 3], self.data['avg'][x - 2]))
            pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 2], self.data['avg'][x - 1]))
            pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 1], self.data['avg'][x]))

            futuro = self.data['avg'][x+1]
            atual = self.data['avg'][x]

            percentfuturo = self.mudanca_percentual(atual, futuro)

            if self._stock not in self._pattern:
                self._pattern[self._stock] = []
                self._pattern[self._stock].append(pattern_array)
            else:
                self._pattern[self.stock].append(pattern_array)

            if self._stock not in self._performances:
                self._performances[self._stock] = []
                self._performances[self._stock].append(percentfuturo)
            else:
                self._performances[self._stock].append(percentfuturo)

            pattern_array = []

            i += 1
            x += 1

    def dia_atual(self):
        return self.data.index.get_loc(self.data[self.data.stock == self._stock].iloc[0].name) + len(self.data[self.data.stock == self._stock])

    def gerar_padrao_atual(self):
        pattern_array = []

        x = self.dia_atual() - 1

        pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 10], self.data['avg'][x - 9]))
        pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 9], self.data['avg'][x - 8]))
        pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 8], self.data['avg'][x - 7]))
        pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 7], self.data['avg'][x - 6]))
        pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 6], self.data['avg'][x - 5]))
        pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 5], self.data['avg'][x - 4]))
        pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 4], self.data['avg'][x - 3]))
        pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 3], self.data['avg'][x - 2]))
        pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 2], self.data['avg'][x - 1]))
        pattern_array.append(self.mudanca_percentual(self.data['avg'][x - 1], self.data['avg'][x]))

        return pattern_array

    def comparar_com_anteriores(self):
        recent = self.gerar_padrao_atual()

        padrao_mais_prox = 0
        distancia_mais_prox = distance.euclidean(recent, self._pattern[self._stock][0])

        for i in range(len(self._pattern[self._stock]) - 1):
            if(i != self.dia_atual() - 1):
                if distance.euclidean(recent, self._pattern[self._stock][i]) < distancia_mais_prox:
                    padrao_mais_prox = i
                    distancia_mais_prox = distance.euclidean(recent, self._pattern[self._stock][i])

        print '\nNome da ação: %s' % self._stock

        print '\nPadrão do dia atual: '
        
        for i, j in enumerate(recent):
            print '%d: %f' % (i, j)

        print '\nPadrão mais próximo dos dias anteriores: ' 
        
        for i, j in enumerate(self._pattern[self._stock][padrao_mais_prox]):
            print '%d: %f' % (i, j)

        print "\nPrevisão de variação: %f" % self._performances[self._stock][padrao_mais_prox]

        x = self.dia_atual()
        valor = self.data['avg'][x] + (self.data['avg'][x] * self._performances[self._stock][padrao_mais_prox]) 

        print "\nMédia de hoje: %f" % self.data['avg'][x]
        print "\nEstimativa para o próximo valor: %f" % valor

        if valor < self.data['avg'][x]:
            print '\nA tendência é que no próximo dia a sua ação irá diminuir de valor'
        else:
            print '\nA tendência é que no próximo dia a sua ação irá aumentar de valor'