a=[1,1,1,2]
a=sorted(a)
c=0
z=0
flag=0
i=0
while i<len(a):
    try:
        while(a[i]==(a[i+1])):
            c+=1
            i+=1
        if(c>0):
            c=0
            z+=1
    except IndexError:
        if(c>0):
            c=0
            z+=1
        break
    i+=1
print(z)
    
