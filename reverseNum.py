num= int(input("enter your number: "))
reversedNum=0

while(num>0):
    digit= num%10
    reversedNum= reversedNum*10+digit
    num= num//10

print(f"reversed number: {reversedNum}")