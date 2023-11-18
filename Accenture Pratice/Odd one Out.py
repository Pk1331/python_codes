"""
Find the odd one out

Input: 3,3,6,6,8,9,8,0,0

Output: 9

Input: 1,6,8,1,8

Output: 6

"""
#Apporach-1
'''
arr=list(map(int,input().split(",")))
for i in range(len(arr)):
    c=0
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            c+=1
    if c==1:
        print(arr[i])
'''
#Apporach-2
arr=list(map(int,input().split(",")))
res=arr[0]
for i in range(1,len(arr)):
    res^=arr[i]
print(res)

