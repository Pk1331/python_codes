"""Count the perfect square numbers

arr=[81,4,6,3,24,11,36,25]

81,4,36,25

ouput: count is:4

"""
import math
arr=list(map(int,input().split()))
count=0
for i in arr:
    z=math.sqrt(i)
    if z.is_integer():
        count+=1
print(count)