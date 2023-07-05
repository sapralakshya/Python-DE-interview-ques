list1=[6,2,7,1]
list2=[9,1,5,4,8]
list3=[]
res1=sorted(list1)
res2=sorted(list2)
i,j=0,0
while i<len(res1) and j<len(res2):
    if res1[i]<res2[j]:
        list3.append(res1[i])
        i=i+1
    elif res1[i]>res2[j]:
        list3.append(res2[j])
        j=j+1
    else:
        list3.append(res1[i])
        list3.append(res2[j])
        j=j+1
        i=i+1
while i<len(res1):
    list3.append(res1[i])
    i=i+1
while j<len(res2):
    list3.append(res2[j])
    j=j+1
print(list3)

