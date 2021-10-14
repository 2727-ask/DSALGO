#Python Program To Print Second Largest Element In Array

a = [2,3,5,-4,1]
m = a[0]
s = 0
for x in a:
    if(x>m):
        s = m
        m = x
    elif(x>s and x!=m):
        s = x
print(s)        
    
