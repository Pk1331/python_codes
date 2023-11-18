"""
Input:

1 2 3 4 5 6 7 8 9

Output:

[2, 4, 6, 8, 1, 3, 5, 7, 9]

"""
arr=list(map(int,input().split()))
l1=[]
l2=[]
for i in arr:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
l1.sort()
l2.sort()
print(l1+l2)