# -*- coding: utf-8 -*-
import pandas as pd
import settings


class Patterns(object):
    def __init__(self, data=None):
        self._data_set = settings.PATH_TO_DATA
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def read_data(self):
        dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')

        self.data = pd.read_csv(self._data_set,
                                delimiter=',',
                                names=['date', 'open', 'high', 'low', 'close', 'volume', 'adj close'],
                                parse_dates=['date'],
                                date_parser=dateparse)

        self.data['avg'] = self.data[['low', 'high']].mean(axis=1)
