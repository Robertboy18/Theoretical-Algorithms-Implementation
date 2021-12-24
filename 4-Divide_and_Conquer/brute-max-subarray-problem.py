def max_sub_prob(arr):
	sum = 0
	actual = 0
	for i in range(len(arr)):
		sum = arr[i]
		for j in range(i+1,len(arr)):
			sum += arr[j]
			actual = max(actual,sum)
	return actual

t = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(max_sub_prob(t))
