import collections as c
def document_distance_problem(s1,s2):
    """
    MIT : Psuedocode
    d(D1,D2) - sequence of words 
    idea : shared words among the two strings
    D[w] : #occurences of each word in D
    We could implement an inner product
    idea 1 : d(D1,D2) = D1.D2 ( but we cant compare between various documents)
    idea 2 : d(D1,D2) = D1.D2/(|D1||D2|)
    """
    l = s1.split(" ")
    t = s2.split(" ")
    d1 = dict(c.OrderedDict((c.Counter(l))))
    d2 = dict(c.OrderedDict((c.Counter(t))))
    print(d1,d2)
    final_dot = 0
    for (k1,v1) in d1.items():
        for (k2,v2) in d2.items():
            if k1 == k2:
                final_dot += v1*v2    
    return (final_dot/(len(d1)*len(d2)))*100

s1 = "abc dsahkhd sa s"
s2 = "aslx abc sa sa z xsha"

print(document_distance_problem(s1,s2))
    
