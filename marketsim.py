__author__ = 'marceloortizdesantana'

import csv
import config
import collections

import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd


reader = csv.reader(open(config.order_file, 'rU'), delimiter = ",")

orders = collections.OrderedDict()
simbols_set = set()
#simbols_set = set("SPX")

for row in reader:
    simbols_set.add(row[3])
    orders[dt.datetime(year=int(row[0]), month=int(row[1]), day=int(row[2]))] = row[3: -1]

ls_simbols = list(simbols_set)

dt_start = orders.keys()[0]
dt_end = orders.keys()[-1]
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['close']
#ls_keys = ['actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_simbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))
na_price = d_data['close'].values
daily = tsu.daily(na_price)
sharpe = tsu.get_sharpe_ratio(daily)
print(sharpe)


print("Details of the Performance of the portfolio :\n")

'''
Details of the Performance of the portfolio :

Data Range :  2011-01-05 16:00:00  to  2011-01-20 16:00:00

Sharpe Ratio of Fund : -0.449182051041
Sharpe Ratio of $SPX : 0.88647463107

Total Return of Fund :  0.998035
Total Return of $SPX : 1.00289841449

Standard Deviation of Fund :  0.00573613516299
Standard Deviation of $SPX : 0.00492987789459

Average Daily Return of Fund :  -0.000162308588036
Average Daily Return of $SPX : 0.000275297459588
'''

#print(d_data)

