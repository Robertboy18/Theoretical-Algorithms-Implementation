def max_peak(arr):
	for i in range(1,len(arr)-1):
		for j in range(1,len(arr[0])-1):
			if arr[i][j]> arr[i+1][j] and arr[i][j] > arr[i-1][j] and arr[i][j] > arr[i][j+1] and arr[i][j] > arr[i][j-1]:
				return arr[i][j]
	return False

k = [[1,3,5],[2,3,4],[123,45,5]]
print(max_peak(k))
