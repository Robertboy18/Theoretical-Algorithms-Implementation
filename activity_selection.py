# 0(nlogn)
def activity_selection(s,f):
    t = set()
    i = 0
    print(i)
    j = 0
    while j < len(f):
        if s[j] >= f[i]:
            i = j
            print(j)
        j += 1
 
s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
print(activity_selection(s,f))
