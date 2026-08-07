def checkPrime(n):
    if(n==1):
        return True
    if(n==2):
        return True

    for i in range (2,n):
        if n%i==0:
            return False

    return True

start= int(input("enter first number: "))
end= int(input("enter second number: "))

print(f"prime numbers between {start} and {end} are: ")

for i in range(start, end+1):
    if checkPrime(i):
        print(i, end= " ")
