# Program to check if given number is prime or not
from math import sqrt
number = int(input("Enter your number:"))
print ("\n")
if number > 1:
    for i in range (2, int(sqrt(number))+ 1):
        if(number % i== 0):
           print(number,"is not a prime number")
           break
    else:
        print(number,"is prime")
else:
    print(number,"is not prime")