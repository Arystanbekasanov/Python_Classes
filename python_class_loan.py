#if I have a loan of 100 000 with 12% yearly, How much should I pay monthly to pay it off in 10 years?


balance = 100000

month = 1
while balance > 0:
    print("Here is your balance: at month {}" .format(balance, month))
    month += 1
    balance = balance + (balance *0.01) - 1500
print("It took you {} years to pay of the balance " .format(balance, month))
