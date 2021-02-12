def sum_n_cubes(n):
	if n <= 1:
		return n
	else:
		return sum_n_cubes(n-1) + n**3

t = 40
print(sum_n_cubes(40))
