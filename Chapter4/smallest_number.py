def smallest_number(arr,f,l):
	if f == l:
		return arr[f]
	else:
		mid = (f+l)//2
		return min(smallest_number(arr,f,mid),smallest_number(arr,mid+1,l))
t = [1,2,3]
print(smallest_number(t,0,2))
