def art_gallery(x):
    # Time 0(N) without sorting else 0(NlogN)
    # Space 0(1)
    # Greedy approach
    l = sorted(x)
    m = 1
    y = x[0]
    for i in range(1,len(x)):
        if abs(y-x[i]) > 1:
            m += 1
            y = x[i] + 1
    return m
            

def main():
    X = [1,2,3,4]
    print(art_gallery(X))
    
main()
