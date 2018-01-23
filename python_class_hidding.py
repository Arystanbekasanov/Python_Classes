class ATM:
    __bal=0
    __limit=500
    def __init__(self, balance, limit):
        #attribute
        self.__bal += balance
        self.__lim = limit
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
        elif amount > self.__limit:
            print("Withdrawal amount exceeds your daily limit")
        else:
            self.__bal -= amount
            print("$ {} was withdrawn ".format(amount))

class CurrencyExchange:
    def transfer_money(self):
        print("Yes, we do transfer money")


class Bank(ATM, CurrencyExchange):
    def __init__(self, balance, limit):
        ATM.__init__(self, balance, limit)

    def loan(self):
        print("Yes, we do provide loans")


# Bank account
bof = Bank(10000, 5000)
bof.show_balance()
bof.deposit(2000)
bof.show_balance()
bof.loan()
bof.transfer_money()

