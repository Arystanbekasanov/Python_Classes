#Function
#convert fahrengeit to celius
# #fah=(celc*1.8) + 32
#We can do that but its long and boring. Thats why we need function
##We can do that but its long and boring. Thats why we need function
#def c_to_f(cel):
#   return (cel*1.8)+32
#n=5
#result=1
#def fact(n):
#    if n==0:
#        return 1
#    else:
#        return n*fact(n-1)
#print("factorial of {5} is: ",fact(5))
#def factorial(num):
#    result = 1
#    for i in range(1,num+1):
#        result=result*i
#    print(result)
#factorial(7)

#Second version of factorial, for not repeat yourself multiple times.
#def fact(num):
#    result =1
#    for i in range(1,num+1):
#        result=result*i
#    print("factorial of {} is {}". format(num,result))
#for i in range(1, 11):
#    fact(i)
#TASK3  Write a function which will calculate fibonacci sequence
#example
#fib(7)
#1 1 2 3 5 8 13 21 . . .
#n=(n-1)+(n-2)
#def fibonacci(number):
#    n1=1
#    n2=1
#    fib=1

#    for i in range(1,11):
#        if i==1:
#            pass
#        elif i==2:
#             pass
#        else:
#             n2=n1
#             n1=fib
#             fib=n1+n2
#        print(fib)

#fibonacci(100)
#next version
#num=int(input("enter the start number here :"))
#end=int(int(input("Enter the end number here:")))
#def fib(n):
#    if n < 2:
#        return n
#    return fib(n-2)+fib(n-1)
#print(fib, range(num, end))
#TAsk4. Solition 1.
#Generate Gausse sequence
#1+2+3+4+.....+n
#n=6
#result=0
#for i in range(1, n+1):
#    result+=i
#print(result)
#SOLUTION2:
#for N6=1+2+3+4+5+6=21
#def gauss_seq(number):
#    if number > 0:
#        return number+gauss_seq(number-1)
#    else:
#        return number
#print(gauss_seq(997))
#














