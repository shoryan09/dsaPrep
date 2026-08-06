num= int(input("enter your number: "))
# num2= int(input("enter your second number: "))

def factorialNum(num):
    result =1
    for i in range(2, num+1):
        result = result*i
    return result

print(f"factorial of a {num} is {factorialNum(num)}")