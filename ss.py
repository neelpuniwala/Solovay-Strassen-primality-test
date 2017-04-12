'''
	Title 		: Solovay Strassen primality test
	Language 	: Python
	By 			: Group-14 (Neel Puniwala  (1401024), Parth Satodiya (1401056))
'''

import random

def solovay_strassen(n, k=10):
	if n == 2 or n == 3:
		return True
	if not n & 1:
		return False
		
	def jacobi(a,n):
		j = 1										#j is jacobi symbol	
		while (a != 0):
			#print '\n'
			while (a%2==0):							# loop till a is even number
				#print j*a,'/',n,', '				# for print jacobi calculations
				j = j * pow(-1,(n*n-1)/8)			# if n=3(mod 8) or n=5(mod 8) then j = -j 
				a = a/2
				
			#print j*a,'/',n,', '					# for print jacobi calculations
			
			if not ( (a-3)%4 or (n-3)%4 ):			# if a=3(mod 4) and n=3(mod 4) then j = -j
				j = -j
				
			a,n = n,a								# interchange(a,n)
			a = a % n								
		return j
		
	for i in xrange(k):
		a = random.randrange(2, n - 1)				# choose any random number from 2 to (n-1)
		x = jacobi(a, n)							# find n's jacobi number
		
		y = pow(a, (n - 1) / 2, n)					# calculate legendre symbol from euler criterion formula
		if y != 1 and y != 0:						
			y = -1
			
		if (x == 0) or (y != x):					# if jecobi and eular criterion formula are not same then the number is not prime
			return False
	
	# if jecobi and eular criterion formula are same for various values of a then the number is prime
	return True

	
n = input('\nEnter number : ')						# enter number for check it's primality
if(n<=1):										
	print 'Number must be >=2'
elif(solovay_strassen(n,10)):
	print n,'is Prime!'
else:
	print n,'is not Prime!'
