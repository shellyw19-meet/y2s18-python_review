


def is_prime(x):
	still_prime = True
	for i in range(2,x//2+1):
		if x % i == 0:
			still_prime = False
	return still_prime
	
	pass


print(is_prime(19))
