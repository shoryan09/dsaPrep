def count_Digits(n):
    if(n==0):
        return 1

    count=0
    n= abs(n)

    while(n>0):
        n= n//10
        count=count+1

    return count

num= int(input("enter a number:"))
print(f"the count is: {count_Digits(num)}")