#nested loop
#outer loop
#first line
for i in range(0, 10):
    #inner loop
        print("*",end=' ')
print("")
#middle lines
for i in range(0, 10):
    print("*", end=' ')
    for i in range(0, 10-2):
        print(" ", end=' ')
    print("*", end=' ')
    print("")
#last line
for j in range(0, 10):
    #inner loop
    print("*",end=' ')


