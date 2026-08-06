char= input("enter your character: ")
if(len(char) != 1):
    print("enter exactly once character")
else:
    if char.isdigit():
        print(f"{char} is a digit")
    elif char.isalpha():
        print(f"{char} is an alphabet")
    else:
        print(f"{char} is a special character")