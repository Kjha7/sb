# -*- coding: utf-8 -*-
from patterns import Patterns
from scipy.spatial import distance

class Stock(Patterns):

    def __init__(self, stock, dataset):
        
        super(self.__class__, self).__init__(dataset)
        self._stock = stock
        self._pattern = {}
        self._performances = {}

    @property
    def stock(self):
        return self._stock

    @property
    def pattern(self):
        return self._pattern

    @property
    def performances(self):
        return self._performances

    def read_dataset(self):
        super(Stock, self).read_dataset()

    def percentchange(self, ant, pos):
        return super(self.__class__, self).percentchange(ant, pos)

    def get_stock_patterns(self):

        pattern_array = []
        
        x = self.data.index.get_loc(self.data[self.data.stock == self._stock].iloc[0].name) + 10
        y = len(self.data[self.data.stock == self._stock])

        i = 0

        while i < y:
            pattern_array.append(self.percentchange(self.data['avg'][x - 10], self.data['avg'][x - 9]))
            pattern_array.append(self.percentchange(self.data['avg'][x - 9], self.data['avg'][x - 8]))
            pattern_array.append(self.percentchange(self.data['avg'][x - 8], self.data['avg'][x - 7]))
            pattern_array.append(self.percentchange(self.data['avg'][x - 7], self.data['avg'][x - 6]))
            pattern_array.append(self.percentchange(self.data['avg'][x - 6], self.data['avg'][x - 5]))
            pattern_array.append(self.percentchange(self.data['avg'][x - 5], self.data['avg'][x - 4]))
            pattern_array.append(self.percentchange(self.data['avg'][x - 4], self.data['avg'][x - 3]))
            pattern_array.append(self.percentchange(self.data['avg'][x - 3], self.data['avg'][x - 2]))
            pattern_array.append(self.percentchange(self.data['avg'][x - 2], self.data['avg'][x - 1]))
            pattern_array.append(self.percentchange(self.data['avg'][x - 1], self.data['avg'][x]))

            future = self.data['avg'][x+1]
            actual = self.data['avg'][x]

            percentFuture = self.percentchange(actual, future)

            if self._stock not in self._pattern:
                self._pattern[self._stock] = []
                self._pattern[self._stock].append(pattern_array)
            else:
                self._pattern[self.stock].append(pattern_array)

            if self._stock not in self._performances:
                self._performances[self._stock] = []
                self._performances[self._stock].append(percentFuture)
            else:
                self._performances[self._stock].append(percentFuture)

            pattern_array = []

            i += 1
            x += 1

    def last_day(self):
        return len(self.data[self.data.stock == self._stock]) - self.data.index.get_loc(self.data[self.data.stock == self._stock].iloc[0].name) - 1

    def get_most_recent_pattern(self):
        pattern_array = []

        x = self.last_day()

        pattern_array.append(self.percentchange(self.data['avg'][x - 10], self.data['avg'][x - 9]))
        pattern_array.append(self.percentchange(self.data['avg'][x - 9], self.data['avg'][x - 8]))
        pattern_array.append(self.percentchange(self.data['avg'][x - 8], self.data['avg'][x - 7]))
        pattern_array.append(self.percentchange(self.data['avg'][x - 7], self.data['avg'][x - 6]))
        pattern_array.append(self.percentchange(self.data['avg'][x - 6], self.data['avg'][x - 5]))
        pattern_array.append(self.percentchange(self.data['avg'][x - 5], self.data['avg'][x - 4]))
        pattern_array.append(self.percentchange(self.data['avg'][x - 4], self.data['avg'][x - 3]))
        pattern_array.append(self.percentchange(self.data['avg'][x - 3], self.data['avg'][x - 2]))
        pattern_array.append(self.percentchange(self.data['avg'][x - 2], self.data['avg'][x - 1]))
        pattern_array.append(self.percentchange(self.data['avg'][x - 1], self.data['avg'][x]))

        return pattern_array

    def compare_with_previous(self):
        recent = self.get_most_recent_pattern()

        closest_pattern = 0
        closest_distance = distance.euclidean(recent, self._pattern[self._stock][0])

        for i in range(len(self._pattern[self._stock]) - 1):
            if(recent != self._pattern[self._stock][i]):
                if distance.euclidean(recent, self._pattern[self._stock][i]) < closest_distance:
                    closest_pattern = i
                    closest_distance = distance.euclidean(recent, self._pattern[self._stock][i])

        print '\nPadrão do dia atual: '
        
        for i, j in enumerate(recent):
            print '%d: %f' % (i, j)

        print '\nPadrão mais próximo dos dias anteriores: ' 
        
        for i, j in enumerate(self._pattern[self._stock][closest_pattern]):
            print '%d: %f' % (i, j)

        print "\nPrevisão de variação: %f" % self._performances[self._stock][closest_pattern]

        x = self.last_day()
        value = self.data['avg'][x] + (self.data['avg'][x] * self._performances[self._stock][closest_pattern]) 

        print "\nMédia de hoje: %f" % self.data['avg'][x]
        print "\nPróximo valor: %f" % value

        if value < self.data['avg'][x]:
            print '\nA tendência é que no próximo dia a sua ação irá diminuir de valor'
        else:
            print '\nA tendência é que no próximo dia a sua ação irá aumentar de valor'

