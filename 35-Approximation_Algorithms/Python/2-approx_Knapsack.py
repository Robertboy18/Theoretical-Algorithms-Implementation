from operator import truediv

"""
Consider a Knapsack instance with n items, each item i having value/profit pi and weight wi
. The capacity
of the knapsack is C. We assume all weights and also the capacity are integers. We assume pi ≤ C for each i,
or else we can just discard it (it won’t fit). We also assume wi > 0 for each i, or else we can trivially add it
without taking up any space in the knapsack.

2 - Approximation Algorithm for Knapsack
"""

def knapSack(C,weights,profits):
    # check if all the items can fit into the capacity
    if sum(weights) < C:
        return sum(profits)
    else:
        final = []
        for i in range(len(weights)):
            final.append([profits[i]/weights[i],weights[i],profits[i]])
        final.sort(key=lambda x: x[0],reverse=True)
        weight, profit = 0, 0
        for i in range(len(final)):
            weight += final[i][1]
            if weight <= C:
                profit += final[i][2]
            else:
                return max(profit,final[i][2])

        
# initialize values
profits = [60, 100, 120]
weights = [10, 20, 30]
C = 50
print(knapSack(C,weights,profits))