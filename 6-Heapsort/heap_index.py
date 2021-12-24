import math
def heap_index(t,i):
	try:
		print("Head Node at : ", t[math.floor(i/2-1)])
		print("Left Child at : ", t[2*i+1])
		print("Right Child at : ", t[2*i + 2])
	except:
		print("No node present")

t = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
heap_index(t,4)
