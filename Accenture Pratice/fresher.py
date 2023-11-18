n,m=map(int,input().split())
res=0
while n>0 and m>0 and n+m>=4:
    if n>m:
        n,m=n-3,m-1
    elif n<m:
        n,m=n-1,m-3
    else:
        n,m=n-2,m-2
    res+=1
print(res)