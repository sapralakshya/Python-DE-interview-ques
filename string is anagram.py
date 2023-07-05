
def anagram_string(str1,str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

str1="karan"
str2="lakshya"
print(anagram_string(str1,str2))



