def minCostClimbingStairs(cost):
    if len(cost) < 2:
        return cost[0]
    dp = [0] * len(cost)
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2,len(cost)):
        dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
    return min(dp[-1],dp[-2])

cost =[1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(cost))