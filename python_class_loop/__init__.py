#Bash
#for i in {1..10}
#do
#echo "Hello $i"
#done

for i in range(1, 11):
    print("Hello" +str(i))

#Bash while loop
#n=1
#while [ $n -lt 11]
#do
#    echo "Hello while loop"
# n=$(($n+1))
#done
n=1
while n < 11:
    print("whileloop Hello {}" .format(n))
    #n=n + 1
    n  += 1

