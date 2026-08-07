def countNums(n):
    count=0
    while(n>0):
        n= n//10
        count +=1
    return count

def armNum(n):
    original= n
    num_Digits= countNums(n)
    total=0

    while(n>0):
        digit= n%10
        total = total + digit ** num_Digits   
        n//=10

    return total== original

num= int(input("enter a number: "))
if(armNum(num)):
    print("this is an armstrong number")
else:
    print("this is not an armstrong number")