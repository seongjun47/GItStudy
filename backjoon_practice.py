n = 0
L = []
i = 0

while n <= 5:
	n += 1
	if n < 3:
		L += [1]
		i += 1
	if n % 2:
		L += [2]
		i += 1
	else:
		L += [3]
	
print(L)
