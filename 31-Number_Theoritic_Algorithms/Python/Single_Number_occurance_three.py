# Bit manipulation
# 0(N) time and 0(1) space
def single_1(A):
    l = '{:032b}'.format(0)
    l = [int(i) for i in l]
    for i in nums:
        m = "{:032b}".format(abs(i))
        for k in range(32):
            l[k] = str(abs(int(l[k])) +abs(int(m[k])))
    for i in range(len(l)):
        l[i] = str(int(l[i])%3)
    t = int("".join(l),2)
    if nums.count(t) == 1:
        return t
    else:
        return -t

# 0(N) space and time
def single_2(A):
    l = {}
    for i in A:
        if i not in l:
            l[i] = 1
        else:
            l[i] +=1
    for k, v in l.items():
        if v == 1:
            return k
   
l  = 10
A = [1,1,2,120,4,1,2,2,4,4,120,120,56]
print(single_1(A))
