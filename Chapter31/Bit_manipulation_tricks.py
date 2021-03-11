def reverse(A):
    # change the format if needed
    g = "{:032b}".format(A)
    return int(g[::-1],2)

def count_1(A):
    # Count the number of 1 bits
    count = 0
    while A:
        A &= (A-1)
        count +=1
    return count

def count_0(A):
    # Count the number of 1 bits way faster than choice 1
    g = "{:032b}".format(A)
    return g.count("1")

def set_bit(A,i):
    # Set the bit 
    return A | (1 << i)

def get_bit(A,i):
    # A & 1 << i just finds the required bit if 0 then 0 & 1 = 0 else 1
    return A & (1 <<i)

def swap(a,b):
    # swap two numbers using bit
    a = a^b
    b = a^b
    a = a^b
    return a,b

def even(A):
    # check even or odd
    return (A&1) == 0

def clear_bit(A,i):
    return A & ~(1<<i)

def add(a,b):
    l = ("{:032b}".format(a))
    m = ("{:032b}".format(b))
    #print(l,m,sep = "\n")
    j = ""
    for i in range(32):
        j = j + str(int(l[i])+int(m[i]))
    #print(j)

def single_1(A):
    l = '{:032b}'.format(0)
    l = [int(i) for i in l]
    for i in A:
        m = "{:032b}".format(i)
        for k in range(32):
            l[k] = str(int(l[k]) +int(m[k]))
    for i in range(len(l)):
        l[i] = str(int(l[i])%3)
    return int("".join(l),2)
            

l  = 10
A = [1,1,2,120,4,1,2,2,4,4,120,120,56]
print(single_1(A))
