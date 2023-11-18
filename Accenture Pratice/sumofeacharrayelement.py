"""sum of digits from array input: arr=[101,234,781,345]

output: res=[2,9,16,12]"""
l=list(map(int,input().split()))
res=[]
for i in l:
    sum=0
    while(i>0):
        sum+=i%10
        i=i//10
    res.append(sum)
print(res)
    