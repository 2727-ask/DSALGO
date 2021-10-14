# 2 Sum Algorithm with Time Complexity 0(n) and Space Complexity 0(n)

arr = [1,0,2,6,7]
target = 1
data = {
    
}
for x,y in enumerate(arr):
    diff = target-y
    if(diff in data):
        print(data[diff],x)
    else:
        data[y] = x
print(data)        
        
    
