def maxThreeNums(a,b,c):
    # return max(a,b,c)
    if(a>b and a >c):
        return a
    elif(b >a and b> c):
        return b
    else:
        return c

print(maxThreeNums(1,2,3))