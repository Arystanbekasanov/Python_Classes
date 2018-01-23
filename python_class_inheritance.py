#Inheritance - Is- A relation
#Class Mammals
#Class Man

#Aggregation - Has -A relation
#Aggregation implies a relationahip where the child can exist independently of the parent
#Example: Class(parent) and Student(child).
#Delete the Class and the Students still exists.

#Composition - Has -A relation
#Composition implies a relationship where the child cannot exist independent of the parent.
#Example: House(parent) and Room(child).
#Rooms don't exist separate to a House

#Polymorphism - overriding
#Polymorphism is based on the greek words Poly(many) and morphism (forms)
#We will create a structure that can take or use many forms of objects.
#Sometimes an objects comes in many types or forms.
# If we have a button, there are many different draw outputs
# (round button, check button, square button, button with image)
# but they do share the same logic: onClick().
# We access them using the same method.
# This idea is called Polymorphism.

class MathCal:
    def addition(self,a, b):
        print("Result of addition is: {}".format(a+b))
    def subtraction(self,a , b):
        print("Result of subtraction is:{}".format(a-b))

class AdvaCal(MathCal):
    def __init__(self):
        self.calc1=MathCal()
    def subtraction(self,a , b):
        self.calc1.subtraction(a, b)
    def multiplication(self,a , b):
        print("Result of multiplication is: {}".format(a*b))

    def division(self,a, b):
        print("Result of division is: {}".format(a / b))
cal1=MathCal()
cal1.subtraction(9,6)
cal1.addition(4,2)
cal2=AdvaCal()
cal2.multiplication(5, 5)
cal2.division(5, 5)
del cal2.calc1
#This line is going to fail, because of aggregation
cal2.subtraction(7,8)