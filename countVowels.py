def countVowels(text):
    text= text.lower()
    vowels= "aeiou"

    for v in vowels:
        count= text.count(v)
        if(count>0):
            print(f"{v}: {count}")

text= input("enter your string: ")
countVowels(text)