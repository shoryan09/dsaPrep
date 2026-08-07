def checkPrime(n):
    if(n==1):
        return True
    if(n==2):
        return True

    for i in range (2,n):
        if n%i==0:
            return False

    return True

num= int(input("enter a number: "))
print(f"{num} is prime: {checkPrime(num)}")