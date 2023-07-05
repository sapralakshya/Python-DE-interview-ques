dict1={"A":1,"B":10,"C":-4,"D":22,"E":6}
max=list(dict1.values())[0]
min=list(dict1.values())[0]
for i in dict1.values():
    if max<=i:
        max=i
    else:
        pass
for i in dict1.values():
    if min>=i:
        min=i
    else:
        pass
print(max,min)
