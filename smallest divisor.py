n = int(input("Enter the number: "))
a = []
for i in range(2, n+1):
    if(n%i==0):
        a.append(i)
a.sort()
print("The divisors: ", a[i])