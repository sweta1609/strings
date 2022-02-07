n=input()
result=''
count=0
i=0
while(i<len(n)):
    k=i
    count = 0
    while k<len(n) and n[i]==n[k]:
        count=count+1
        k+=1
    if count>1:
        result=result+n[i]+str(count)
    else:
        result=result+str(n[i])
    i=k    
print(result)
