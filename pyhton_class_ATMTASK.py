#TASK ATM
class ATM:
    balance = 1000

while True:
        withdraw = int(input("How much do you want to withdraw? :"))
        if withdraw <= balance:
            balance -= withdraw
            print("Here is your new balance: {}" .format(balance))
        else:
            print("You do not have enough balance to do this transaction")
            break
