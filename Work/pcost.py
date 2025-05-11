# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):


    cost_a = 0
    with open(filename, 'rt') as f:
        try:
            headers = next(f).split(',')
        except ValueError:
            print(headers)

        for line in f:
            try:
                row = line.split(',')
                s_cost = int(row[1]) * float(row[2])
                cost_a += s_cost
            except ValueError:
                print('Bad row', row)
        return cost_a

import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter File Name:')


cost = portfolio_cost(filename)
print('Total cost: ',cost)
