# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.dates as mdates

data = pd.read_csv('data/dataset.csv',
                   delimiter=',',
                   names=['date', 'stock', 'min', 'max'],
                   converters={0: mdates.strpdate2num('%Y%m%d')})

data['avg'] = data[['min', 'max']].mean(axis=1)

patterns = {}
performances = {}


def percentchange(ant, pos):
    return round(((float(pos)-ant)/abs(ant))*100, 2)


def getpattern(stock):

    global patterns, performances

    pattern = []
    x = data.index.get_loc(data[data.stock == stock].iloc[0].name) + 10
    y = len(data[data.stock == stock]) - 30

    i = 0

    while i < y:
        pattern.append(percentchange(data['avg'][x - 10], data['avg'][x - 9]))
        pattern.append(percentchange(data['avg'][x - 9], data['avg'][x - 8]))
        pattern.append(percentchange(data['avg'][x - 8], data['avg'][x - 7]))
        pattern.append(percentchange(data['avg'][x - 7], data['avg'][x - 6]))
        pattern.append(percentchange(data['avg'][x - 6], data['avg'][x - 5]))
        pattern.append(percentchange(data['avg'][x - 5], data['avg'][x - 4]))
        pattern.append(percentchange(data['avg'][x - 4], data['avg'][x - 3]))
        pattern.append(percentchange(data['avg'][x - 3], data['avg'][x - 2]))
        pattern.append(percentchange(data['avg'][x - 2], data['avg'][x - 1]))
        pattern.append(percentchange(data['avg'][x - 1], data['avg'][x]))

        future = data['avg'][x+10:x+20]
        actual = data['avg'][x]

        try:
            avgfuture = reduce(lambda x, y: x+y, future)/len(future)
        except Exception, e:
            print str(e)
            avgfuture = 0

        percentFuture = percentchange(actual, avgfuture)

        if stock not in patterns:
            patterns[stock] = []
            patterns[stock].append(pattern)
        else:
            patterns[stock].append(pattern)

        if stock not in performances:
            performances[stock] = []
            performances[stock].append(percentFuture)
        else:
            performances[stock].append(percentFuture)

        pattern = []

        i += 1
        x += 1

getpattern('AA')
print patterns['AA']
print performances['AA']
