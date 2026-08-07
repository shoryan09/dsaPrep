def sumOfDigits(n):
    if(n==0):
        return 0

    totalSum=0
    n = abs(n)

    while(n>0):
        digit= n%10
        totalSum= totalSum+digit
        n=n//10

    return totalSum

num= int(input("enter your number: "))
print(f"sum is {sumOfDigits(num)}")