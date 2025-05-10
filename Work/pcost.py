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
            row = line.split(',')
            s_cost = int(row[1]) * float(row[2])
            cost_a += s_cost
        return cost_a


cost = portfolio_cost('Data/portfolio.csv')
print('Total cost: ',cost)
