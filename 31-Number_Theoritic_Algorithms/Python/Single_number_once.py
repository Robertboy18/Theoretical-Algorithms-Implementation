# Bit wise 
# Xor 
# time 0(N) and space 0(1)
def singleNumber(A):
  t = 0
  for i in A:
      t = t ^ i
  return t

A = [1,2,3,4,2,3,4]
print(singleNumber(A))

  
