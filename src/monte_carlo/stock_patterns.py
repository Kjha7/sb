# -*- coding: utf-8 -*-
from patterns import Patterns
from math import sqrt, pow
from settings import settings


class Stock(Patterns):
    def __init__(self):
        super(self.__class__, self).__init__()
        self._pattern = []
        self._performances = []
        self.read_data()
        self.generate_patterns()
        self.compare()

    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self, value):
        self._pattern.append(value)

    @property
    def performances(self):
        return self._performances

    @performances.setter
    def performances(self, value):
        self._performances.append(value)

    @staticmethod
    def euclidean_distance(p, q):
        summatory = 0
        for i in range(len(p)):
            summatory += pow(q[i] - p[i], 2)
        return sqrt(summatory)

    @staticmethod
    def percent_change(ant, pos):
        return (float(pos) - ant) / abs(ant)

    def read_data(self):
        super(self.__class__, self).read_data()

    def generate_patterns(self):
        pattern_array = []

        x = 1
        y = len(self.data) - 11

        i = 0

        while i < y:
            pattern_array.append(self.percent_change(self.data.avg[x + 10], self.data.avg[x + 9]))
            pattern_array.append(self.percent_change(self.data.avg[x + 9], self.data.avg[x + 8]))
            pattern_array.append(self.percent_change(self.data.avg[x + 8], self.data.avg[x + 7]))
            pattern_array.append(self.percent_change(self.data.avg[x + 7], self.data.avg[x + 6]))
            pattern_array.append(self.percent_change(self.data.avg[x + 6], self.data.avg[x + 5]))
            pattern_array.append(self.percent_change(self.data.avg[x + 5], self.data.avg[x + 4]))
            pattern_array.append(self.percent_change(self.data.avg[x + 4], self.data.avg[x + 3]))
            pattern_array.append(self.percent_change(self.data.avg[x + 3], self.data.avg[x + 2]))
            pattern_array.append(self.percent_change(self.data.avg[x + 2], self.data.avg[x + 1]))
            pattern_array.append(self.percent_change(self.data.avg[x + 1], self.data.avg[x]))

            actual_value = self.data.avg[x]
            future_value = self.data.avg[x - 1]

            percent_future = self.percent_change(actual_value, future_value)

            self.pattern = pattern_array
            self.performances = percent_future

            pattern_array = []

            i += 1
            x += 1

    def get_current(self):
        pattern_array = []

        x = 0

        pattern_array.append(self.percent_change(self.data.avg[x + 10], self.data.avg[x + 9]))
        pattern_array.append(self.percent_change(self.data.avg[x + 9], self.data.avg[x + 8]))
        pattern_array.append(self.percent_change(self.data.avg[x + 8], self.data.avg[x + 7]))
        pattern_array.append(self.percent_change(self.data.avg[x + 7], self.data.avg[x + 6]))
        pattern_array.append(self.percent_change(self.data.avg[x + 6], self.data.avg[x + 5]))
        pattern_array.append(self.percent_change(self.data.avg[x + 5], self.data.avg[x + 4]))
        pattern_array.append(self.percent_change(self.data.avg[x + 4], self.data.avg[x + 3]))
        pattern_array.append(self.percent_change(self.data.avg[x + 3], self.data.avg[x + 2]))
        pattern_array.append(self.percent_change(self.data.avg[x + 2], self.data.avg[x + 1]))
        pattern_array.append(self.percent_change(self.data.avg[x + 1], self.data.avg[x]))

        return pattern_array

    def compare(self):
        recent = self.get_current()

        prox = 0
        dist_prox = self.euclidean_distance(recent, self.pattern[0])

        for i in range(1, len(self.pattern)):
            dist_comp = self.euclidean_distance(recent, self.pattern[i])
            if dist_comp < dist_prox:
                prox = i
                dist_prox = dist_comp

        print '\nAção: ' + settings.STOCK
        print '\nDia atual: ' + str(self.data.date[0])

        print '\nPadrão do dia atual: '

        for i, j in enumerate(recent):
            print '%d: %f' % (i, j)

        print '\nDia anterior mais próximo: ' + str(self.data.date[prox])
        print '\nPadrão mais próximo dos dias anteriores: '
        for i, j in enumerate(self.pattern[prox]):
            print '%d: %f' % (i, j)

        print "\nPorcentagem de variação: %f" % self.performances[prox]

        x = 0
        val = self.data.avg[x] + (self.data.avg[x] * self.performances[prox])

        print "\nMédia de hoje: %f" % self.data.avg[x]
        print "\nEstimativa para o próximo valor: %f" % val

        if val < self.data.avg[x]:
            print '\nBaseada em padrões anteriores, a tendência é que no próximo dia a sua ação irá diminuir de valor'
        else:
            print '\nBaseada em padrões anteriores, a tendência é que no próximo dia a sua ação irá aumentar de valor'
