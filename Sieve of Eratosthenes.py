n=int(input("Enter the number: "))
sieve=set(range(2,n+1))
while sieve:
    prime=min(sieve)
    print(prime,"\t")
    temp=set(range(prime,n+1,prime))
    sieve-=temp
print()