n = int(input("Enter the number: "))
temp = n
c = 0
while n > 0:
    rem = n%10
    c = c*10+rem
    n = n//10
if(temp==c):
    print("The number is palindrome: ", temp)
else:
    print("The number isn't palindrome: ", temp)



