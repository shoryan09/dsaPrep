num1= int(input("enter your number: "))
num2= int(input("enter your number: "))
num3= int(input("enter your number: "))

# if num1 > num2:
#     num1, num2= num2, num1
# if num1 > num3:
#     num1, num3= num3, num1
# if num2 > num3:
#     num2, num3= num3, num2

result = sorted([num1, num2, num3])

print(f"ascending order {num1}, {num2}, {num3}")
print(f"Ascending order: {result[0]}, {result[1]}, {result[2]}")
