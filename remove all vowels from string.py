str="lakshya"
vowels=['a','e','i','o','u','A','E','I','O','U']
result=""
for i in str:
    if i not in vowels:
        result=result+i
print(result)

