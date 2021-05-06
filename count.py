def countConsecutive(number):
	
	# constraint on values of L gives us the
	# time Complexity as O(N^0.5)
	count = 0
	L = 1
	while( L * (L + 1) < 2 * number):
		a = (1.0 * number - (L * (L + 1) ) / 2) / (L + 1)
		if (a - int(a) == 0.0):
			count += 1
		L += 1
	return count

number = 15000000000000
print(countConsecutive(number))
