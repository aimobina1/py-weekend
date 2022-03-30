#sinx
import math

x = 2
e_to_2 = 0
for i in range(6):
    e_to_2 += x**i/math.factorial(i)
    
print(e_to_2)

#2gcd
numOne=int(input("enter the first number:"))
numTwo=int(input("enter the second number:"))
gcd = gcd(numOne , numTwo)
print ("The gcd of num 1 and num 2 is :" , gcd)


#3-Program to check Armstrong numbers in a certain interval
lower = 1
upper = 10000
for num in range(lower, upper + 1):
   # order of number
   order = len(str(num))
   # initialize sum
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)

#4-root- The function is x^3 - x^2 + 2
def func( x ):
	return x * x * x - x * x + 2

def derivFunc( x ):
	return 3 * x * x - 2 * x

# Function to find the root
def newtonRaphson( x ):
	h = func(x) / derivFunc(x)
	while abs(h) >= 0.0001:
		h = func(x)/derivFunc(x)
		
		# x(i+1) = x(i) - f(x) / f'(x)
		x = x - h
	
	print("The value of the root is : ",
							"%.4f"% x)

x0 = -20 # Initial values assumed
newtonRaphson(x0)

