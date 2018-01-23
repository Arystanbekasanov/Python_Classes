#input a number, calculate grade
#A 90-100%
#B 80-90%




score =int(input("Please enter your score from (0-100):"))
if 90< score <=100:
    print("Your score is:  A ")
elif 80< score <89:
    print("your score is: B")
elif 70< score <79:
    print("Your score is: C")
elif  60< score <69:
    print("your score is D , keep it up")
elif 0< score <59:
    print("your score is F, You failed man")

