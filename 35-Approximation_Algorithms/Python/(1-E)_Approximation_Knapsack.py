from operator import truediv
import math

def Knapsack_Original(W, wt, val, n):
    """
    Consider a Knapsack instance with n items, each item i having value/profit pi and weight wi
. The capacity of the knapsack is C. We assume all weights and also the capacity are integers. We assume pi ≤ C for each i,
or else we can just discard it (it won’t fit). We also assume wi > 0 for each i, or else we can trivially add it
without taking up any space in the knapsack
    """
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]

def Knapsack_2_approx(C,weights,profits):
    # check if all the items can fit into the capacity
    """
    Before proceeding with the approximation algorithm, simply note the following very trivial observation: Suppose
wi = 1 for all items i. Then the optimum solution will just pack the min{n, C} most profitable items.
Here is a greedy 2-approximation:
• If we can fit all items in the knapsack, then do it (and stop the algorithm).
• Sort the items so p1/w1 ≥ p2/w2 ≥ . . . ≥ pn/wn.
• Pack the items greedily in this order until you can’t fit the next item. That is, let k be the largest integer
with w1 + w2 + . . . + wk ≤ C.
• Return the more profitable of the following two solutions {1, . . . , k} and {k + 1}. Both are feasible: the
first is by construction and the second is because we assume all items fit by themselves
Running Time: O(n log n) due to sorting. Everything else takes linear time
    """
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

def choice(i,C,weights,profits):
    # use any upper bound value ( max profits or use the 2 approximation one)
    if i == 1:
        return max(profits)
    else:
        return Knapsack_2_approx(C,weights,profits)

def Knapsack_different(C,weights,profits_changed,P):
    """
    Let f(i, p) be the minimum-weight subset of items {1, . . . , i} that gets profit exactly p. If there is no such
subset with profit exactly p, let f(i, p) = ∞. The following recurrence relates these values. For 0 ≤ i ≤ n and
0 ≤ p ≤ P, we have
f(i, p) =   0 if i = p = 0
            ∞ if i = 0, p > 0
            f(i, p − 1) if i > 0, pi > p
            min{f(i − 1, p), wi + f(i − 1, p − pi)} if i > 0, pi ≤ p
Correctness is straightforward so it will not be argued here. The running time is O(n·P) since there are O(n·P)
subproblems and each takes O(1) time to calculate if we use dynamic programming
    """
    final = [[0 for x in range(P + 1)] for x in range(len(weights) + 1)]
    for i in range(len(weights) + 1):
        for p in range(P + 1):
            if i == 0 and p > 0:
                final[i][p] = 10e10
            elif i == 0 and p == 0:
                final[i][p] = 0
            elif profits_changed[i-1] <= p:
                final[i][p] = min(weights[i-1] + final[i-1][p-profits_changed[i-1]], final[i-1][p])
            else:
                final[i][p] = final[i][p-1]
    return final[len(weights)][P]

def FPTAS_Knapsack(C,weights,profits,epsilon,max_bound,dp_choice):
    """
    1 - Use the 2-approximation to find p^ with OPT/2 ≤ p^ ≤ OPT
    2 -  ∆ ← n/(p^*epsilon)
    3 - scale all profits_i = ceil(delta*profits_i)
    4 - Use the dynamic programming approach to find the optimal solution
    5-  Return the optimal solution
    Running Time: Computing ˆp takes O(n log n) time. Running the DP algorithm takes O(n · P) = O(n · n/epsilon) = O(n^2/epsilon) time for
the given choice of P. So the total running time is O(n^2/epsilon)
    Hence a 1-epsilon approximation algorithm is O(n^2/epsilon)
    """
    delta = len(weights)/(epsilon*choice(max_bound,C,weights,profits))
    profits_changed = [math.floor(x*delta) for x in profits]
    P = math.floor(2*len(weights)/epsilon)
    if dp_choice == 1:
        return Knapsack_Original(C,weights,profits_changed,len(weights))
    else:
        return Knapsack_different(C,weights,profits_changed,P)
 
        
# initialize values
profits = [12, 16, 4,8]
weights = [3, 4, 5, 2]
C = 10
epsilon = 0.5
dp_choice = 1 # 1 for original dp , 2 for different dp 
max_bound = 1 # max value in the profits array, 2 for using the 2 approx optimal value
print("Original Knapsack Optimal value ",Knapsack_Original(C, weights, profits, len(weights)))
print("2 - Approx Knapsack value ", Knapsack_2_approx(C, weights, profits))
print(" 1 - Epsilon approx knapsack value ",FPTAS_Knapsack(C,weights,profits,epsilon,max_bound,dp_choice))