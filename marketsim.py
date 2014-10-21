__author__ = 'marceloortizdesantana'

import csv
import config

reader = csv.reader(open(config.order_file, 'rU'), delimiter = ",")

for row in reader:
    print(row)


