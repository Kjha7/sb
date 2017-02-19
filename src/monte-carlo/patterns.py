# -*- coding: utf-8 -*-
import pandas as pd 
import matplotlib.dates as mdates

class Patterns(object):

	def __init__(self, dataset):
		self._dataset = dataset

	def read_dataset(self):
		self.data = pd.read_csv(self._dataset,
                   				delimiter=',',
                   				names=['date', 'stock', 'min', 'max'],
                   				converters={0: mdates.strpdate2num('%Y%m%d')})

		self.data['avg'] = self.data[['min', 'max']].mean(axis=1)

	def percentchange(self, ant, pos):	
		return (float(pos)-ant)/abs(ant)