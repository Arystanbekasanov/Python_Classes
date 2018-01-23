#Python lets get started 13/01/2018. Python class with Islam baike.
#OOP=Object oriented programming. Procedural vs OOP.

# #variable scope
# def mat(a, b):
#     #local variable
#     result = a+b
#     print(message)
#     return result
# def class_print(m1 , m2):
#     result=m1 + m2
#     return result
#
# #Global variable
# message= "Addition"
# print(mat(5, 6))
# print(mat(7, 7))
# #Using functions is very easy to manage your code. If can edit just one thinfg and change whole code.
# def mat(a, b):
#     #local variable
#     result = a-b
#     print(message)
#     return result
#
# #Global variable
# message= "Subtraction"
# print(mat(15, 9))
# print(class_print("Hello", "Ararat"))

# def test_func():
#     print("I like"  + fruit)
#
# fruit='Apple'
# test_func()
# def test_func():
#     #local variable
#     fruit='mellon'
#     print("I like"  + fruit)
#Global variable
# fruit="apple"
# test_func()
# fruit="Watermellon"
# print("I really like" + fruit)
#Class is a template to create objects
#Object: an instance of a class
#Instantiate: create an instance of a class
# __init__ is the constructor for a class. The self parameter refers to the instance of the object
#Method: function defind in a class
#The difference between function and a method is that it uses a self parameter
#Attribute: a variable bound to an instance of a class it is suggested to use uppercase names for classes
#_self_ as it suggests, refers to itself- the object which has called the method.
#  That is, if you have N objects calling the method, then self.a will refer to a separate instance of the variable
# for each of the N objects. Imagine N copies of the variable a for each object
#__init__ is what is called as a constructor in other OOP languages such as C++/Java.
# The basic idea is that it is a special method which is automatically called when an object of that Class is created
#1 example. Car is object, self is class.
# class Car:
#     wheels=5
#     #method is a function defined in a class
#     def __init__(self, models):
#         print("This is a new car," + models)
#
# camry = Car("Camry")
# print("My camry has {} wheels".format(camry.wheels))
# sienna = Car("Sienna")
# print("My sienna has {} wheels".format(sienna.wheels))
#2 example.
# class Car:
#     wheels=5
#     #method is a function defined in a class
#     def __init__(self, models):
#         print("This is a new car ," + models + " , is has {} wheels".format(self.wheels))
# camry = Car("Camry")
# sienna =Car("Sienna")
#3.example
# class MyClass(object):
#     num = 123
#     def __init__(self):
#         self.num = 345
#
# a = MyClass()
# print(a.num)
# print(MyClass.num)
#4. example.
# class Car:
#     wheels=4
#     #special initializor method
#     #__init__ is a special method which is automatically called every time when u create a new object off of a class
#     def __init__(self, models):
#         print("This is a new car ," + models)
#     #regular method
#     def init_car(self, models):
#         print("this is a new car," + models)
#     def get_wheels(self):
#         print("That car has {} wheels " .format(self.wheels))
# car1= Car("Ferrari")
# car1.get_wheels()
# car1.init_car("Camry")
#5.example
# class Car:
# #__init_ is a special initializer method
#     def __init__(self, name):
#         print("This is a new car," + name)
# #__str__ is special method which is automatically called when u print an object
#     def __str__(self):
#         return "This is a Car object"
#     #__del__ is a special method which is automatically called when u destroy the object
#     def __del__(self):
#             print("Please don't kill me")
#
#
# car1= Car("Camry")
# print(car1)
# del car1
#N6 example:
#Let's say you have a class ClassA which contains a
#method MethodA defind as:
# class ClassA:
#     def methodA(self, arg1):
#         print("This is just a dummy message:" +arg1)
# #and ObjectA is a instance of this class:
# ObjectA=ClassA()
# ObjectA.methodA("Aban")
# #Now when ObjectA.method(arg1) is called
# #Python internally converts it for you as:
# ClassA.methodA(ObjectA, "Aban")
# #The self variable refers to the object itself.
# ObjectB=ClassA()
# ObjectB.methodA("Winterbeck")
# ClassA.methodA(ObjectB, "Winterbeck")






















