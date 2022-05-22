def isPrime(numbers):
    if numbers == 1:
        return True
    if numbers == 2:
        return False
    for i in range (2, numbers//2 + 1):
    		if numbers % i == 0: 
    			return False
    else: 
    	return True
 

print(isPrime(10))





def testIsPrime():
	assert(testIsPrime(1) == True)
	assert(testIsPrime(2) == False)
	assert(testIsPrime(17) == True)
	assert(testIsPrime(40) == False)
	assert(testIsPrime(29) == True)









