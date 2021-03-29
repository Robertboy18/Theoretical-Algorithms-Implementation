import collections as c 
def knapsack_fractional(p,w,M):
    l = c.defaultdict(list)
    for i in range(len(p)):
        l[round(float(p[i]/w[i]),2)].append(p[i])
        l[round(float(p[i]/w[i]),2)].append(w[i])
    m = dict(sorted(l.items(),key = lambda x : x[0],reverse= True))
    final = 0
    for __,v  in m.items():
        if M - v[1] >= 0:
            final += v[0]
            M = M - v[1]
        else:
            final += float(M/v[1])*v[0]
            M = M - int(v[0] - float(M/v[1]))
            break    
    return final

def main():
    p = [25,24,15]
    w = [18,15,10]
    M = 20
    print(knapsack_fractional(p,w,M))
