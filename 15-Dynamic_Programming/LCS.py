def LCS_recurrsive(x,y,i,j):
  # Time (0(2^n))
    if i == 0 or j == 0:
        return 0
    elif x[i-1] == y[j-1]:
        return 1 + LCS_recurrsive(x,y,i-1,j-1)
    else:
        return max(LCS_recurrsive(x,y,i,j-1),LCS_recurrsive(x,y,i-1,j))
    
def LCS_dp(x,y):
  # Time 0(len(x) * len(y))
    dp = [[0]*(len(y)+1) for __ in range(len(x)+1)] 
    for i in range(len(x)+1):
        for j in range(len(y)+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i-1] == x[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    return dp[len(x)][len(y)]
                
    

def main():
    x = "abc"
    y = "ab"
    print(LCS_recurrsive(x,y,len(x),len(y)))
    print(LCS_dp(x,y))
