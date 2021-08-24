n = int(input("Enter the number: "))
temp = 0
while(n>0):
    x=n%10
    temp=temp+x
    n=n//10
print("The sum of digits: ", temp)

