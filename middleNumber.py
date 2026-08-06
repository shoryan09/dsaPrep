num1= int(input("enter your number: "))
num2= int(input("enter your number: "))
num3= int(input("enter your number: "))

nums= [2,4,5,43,235,35,3,65,3,23]

count=0
for num in nums:
    count +=1

middle_index= count //2

for i, num in enumerate(nums):
    if i== middle_index:
        print(f"middle element: {num}")
        break