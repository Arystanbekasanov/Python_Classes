#1#String and how we can work strings
# str = "Hello world!"
#
# print(str)
# print(str[0])
# print(str[2:5])
# print(str[0:10])
# print(str + "TEST")

#2#Operators:+, -, /. (ctrl+/ to put#)
# number=10
# number-=2
# print(number)
# number+=43
# print(number)
# number//=2
# print(number)
# number = 5
# result=number >3
# print(result)
#3# Nesta condition. Condiotion in condition.(if incide of if)
# succes=number > 4
# if succes:
#     if str:
#         print("its greater than")
#     else:
#         print("string has no value")
# else:
#     print("its less than 3")
#4#
# string = "Chocolate chunk cookie mmm daadaaddad"
# string_with_lines = """     This delicious Otis Spunkmeyer
#              baked cookie is loaded with the
#              finest quality ingedients."""
# print(string_with_lines)
# for i in range(0, len(string)):
#     print(i)
# for i in string:
#     print(i)
# list =[]
# for i in range(1, 4):
#     num=input("Please enter any number :".format(i))
#     list.append([i])
# print(list)
# names =[]
# for i in range(0, 4):
#     nam=input("Please enter the names :")
#     names.append(nam)
# print(names)
# ch=input("Which letter would you like to check?:")
# ch.lower()
#
# for name in names:
#     if ch in name.lower():
#         print("this names has {}".format(ch))
#     else:
#         print("This names has no {} ".format(ch))
#Input numbers and give the average of them.#We can use "INSERT mode or APPEND mode" "The difference are in two points clear:APPEND will only add the record if at the end of statement
#INSERT will insert anywhere you want i.e if your table have 10 column you can insert in 5 column only but in append you can't.
#in append both your data and the table should have same columns means insert data in row level rather than in column level
# #and it's also true you cannot use insert if your table have data if it's empty then only you can do use insert.
# list =[]
# average=0
# for i in range(0, 5):
#     number=input("Please enter the number: ")
#     list.insert(0,int(number))
# print("This is the list:", list)
# for i in range(0, len(list)):
#     average+=list[i]
# print("Addition of those numbers: ",average)
# print(" Average of those numbers is: {}".format(average / len(list)))
#TASK 11/01/2018

# letters =[]
# for i in range(0, 4):
#     let=input("Please enter the letters :")
#     letters.insert(0, let)
# print(letters)
# num=0
# for i in letters:
#     num +=1
# print(num)
#
# ch=input("Which letter would you like to check?:")
# ch.lower()
# ch.upper()
# for name in letters:
#     if ch in name.lower():
#         print("this letters has lowercase {}".format(ch.lower()))
#     elif ch in name.upper():
#         print("This letters has uppercase {}".format(ch.upper()))
#     else:
#         print("This letters has no {} ".format(ch.lower()))
#TASK /1.0 How to find a vowels and consonants using function.
# list=['Bash is sucks','a','v','c']
# vowels='aieuyo'
# def findAVowel(list):
#     for char in list:
#         if char in vowels:
#             print("{} :is a vowel".format(char))
#         else:
#             print("{} :is not a vowel".format(char))
#
# findAVowel(list)
#while loop. true or false
# # list = ["student1","stud2","stud3","stud4"]
# while len(list) > 0:
#     print(list)
#     choose=input("Please choose from 1-{}: ".format(len(list)))
#     list.pop(int(choose)-1)
#     print(list)
# for i in range(0, len(list)):
#     choose=input("Please choose from 1-{} :".format(len(list)))
#     list.pop(int(choose)-1)
#     print(list)
#TASK with For loop
# names =[]
# for i in range(0, 4):
#     nam=input("Please enter the names :").lower()
#     if nam!="bob":
#         names.append(nam)
#         print(names)
#     else:
#         print("We detected bad name actually:!")
# print(names)
#with While loop
# list=[]
# while True:
#     name=input("please enter the name:".format(list)).lower()
#     if name!="bob":
#         list.append(name)
#         print(list)
#     else:
#         print("We detected bad name")
#         break
# print(list)
# #TASk. create a list inside a list. Go inside the list. Compare the length and print one with longest length
# list = [[1,2,3], [1,2,3,4],[1,3,5,5,6,8,9,0], [1,2,3,4,5], [1,2,3,4,5,6]]
# most = list[0]
# for i in range(1,len(list)):
#     if len(most) < len(list[i]):
#         most=list[i]
# print(most)
#How to do prev example with While loop?
# list = [[1,2,3], [1,2,3,4],[1,3,5,5,6,8,9,0], [1,2,3,4,5], [1,2,3,4,5,6]]
# most=list[0]
# while len(list) < len(list[4]):
#     print(list)
#     breakclass ATM:
