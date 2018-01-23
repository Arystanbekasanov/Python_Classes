from math import gcd

#3 digit lcm calculation
h=input("(1) 2 Digit LCM Or \n(2) 3 Digit LCM\n :")
if h == "2":
    while True:
        def lcm(num1,num2,num3):
            gcd2 = gcd(num2,num3)
            gcd3 = gcd(num1,gcd2)

            lcm2 = num2*num3 // gcd2
            lcm3 = num1*lcm2 // gcd(num1, lcm2)
            return lcm3

        n1=int(input("Please enter number1: "))
        n2=int(input("Please enter number 2: "))
        n3=int(input("Please enter number 3:"))
print("LCM of: {}"sr(num1) "And" str(num2)"And"str(num3) "Is"str(lcm(num1,num2,num3))
