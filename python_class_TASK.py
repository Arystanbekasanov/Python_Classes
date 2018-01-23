#Task1
#Research about regular expressions
#And write a code which is validates IP address
#10.0.12.222 is valid IP
#while 10.0.12.2222 is no

#Task2 Work with ATM code
#Perfect out ATM code
#Add deposit , check balance option
#funtion overloading
#def hello(name= 'student'):
#    print("hello" +name)
#hello()
#hello('Bob')
#Function TASK
#Task1: Create a function which inputs 3 arguments and returns the least common multiple of three integers.
#Given x,y and z, the least common multiple is the smallest positive integer that has l , m and n as factors.
#Example:Common least multiple of 2,3 and 4 is 12. Найти минимально делимую цифру.
from math import gcd
h=input("(1) 2 Digit GCD Or \n(2) 3 Digit LCM\n :")
if h == "2":
    while True:
        def lcm(m, l, n):
            gcd2 = gcd(l, n)
            gcd3 = gcd(m,gcd2)
            lcm2 = l*n// gcd2
            lcm3 = m*lcm2// gcd(m,lcm2)
            return lcm3

        m= int(input("Number 1: "))
        l= int(input("Number 2: "))
        n= int(input("Number 3: "))
        print("The LCM(Least common Multiple) Of " + str(m)+ " And " + str(l) + " And " + str(n) + " Is " + str(lcm(m, l, n)))
        break

if h == "1":
    while True:
        def gcd(num1,num2):
            for i in range(1, num1*num2+1):
                if i%num1==0 and i%num2==0:
                    print("GCD(greatest common multiple) is :{}".format(i))
                    break
        n1=int(input("Please enter number1: "))
        n2=int(input("Please enter number 2: "))
        gcd(n1,n2)
