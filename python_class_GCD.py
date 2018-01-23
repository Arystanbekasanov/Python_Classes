from math import gcd

#3 digit lcm calculation
h=input("(1) 2 Digit LCM Or \n(2) 3 Digit LCM\n :")


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
        print("The LCM Of " + str(m)+ " And " + str(l) + " And " + str(n) + " Is " + str(lcm(m, l, n)))