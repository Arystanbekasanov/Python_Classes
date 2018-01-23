#oop with atm

# class ATM:
#     bal =250
#     def __init__(self, balance):
#         #attribute
#         self.bal +=balance
#         print("Your deposit amount is : {}".format(balance))
#     #Getter. it gets a value from the class/object.
#     def show_balance(self):
#         print("This is your balance: {}".format(self.bal))
#
# chase = ATM(500)
# chase.show_balance()
# bof = ATM(400)
# bof.show_balance()
#
# mb = ATM(600)
# mb.show_balance()
class ATM:
    __bal=100
    #We can rename the name by using:REFACTOR=>rename.
    # A SINGLE underscore before a name is used to specify that the name is to be treated as “private” by a programmer.
    #  It’s kind of* a convention so that the next person (or yourself) using your
    # code knows that a name starting with _ is for internal use.
#The use of DOUBLE underscore (__) in front of a name (specifically a method name) is not a convention;
    #  it has a specific meaning to the interpreter.
    # Python mangles these names and it is used to avoid name clashes with names defined by subclasses.
    #  As the Python documentation notes, any identifier of the form __spam (at least two leading underscores,
    #  at most one trailing underscore) is textually replaced with _classname__spam,
    #  where classname is the current class name with leading underscore(s) stripped.

    def __init__(self, balance):
        #attribute
        self.__bal += balance
        #self.show_balance()
    #Getter. it gets a value from the class/object.
    def show_balance(self):
        print("This is your balance: {}".format(self.__bal))
    #Setter method - sets value
    def deposit(self, amount):
        self.__bal +=amount
        depo=input("How much would you like to deposit?: ".format(amount))
        print("${} was deposited ".format(amount))
        #self.show_balance()
    #def withdrawal() TASK/SETTER
    def withdrawal(self, amount):
        withdrawal=input("How much would you like to withdraw? :".format(amount))
        if amount > self.__bal:
            print("You do not have enough balance to do this transaction")
        else:
            self.__bal -= amount
            print("$ {} was withdrawed ".format(amount))
chase = ATM(20000)
chase.show_balance()
chase.__bal=500000
chase.deposit(100)
chase.show_balance()
chase.withdrawal(400)
chase.show_balance()
