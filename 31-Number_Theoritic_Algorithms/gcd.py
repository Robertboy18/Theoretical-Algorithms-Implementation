# Time Complexity : n^2 lg(n) 2^O(log* n) where n = log(ab)
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(12, 8))
print(gcd(24, 16))
print(gcd(81, 27))