def GCD(num1,num2):
    if num1==0:
        return num2
    else:
        return GCD(max(num1,num2)%min(num1,num2),min(num1,num2))
print(GCD(4,8))