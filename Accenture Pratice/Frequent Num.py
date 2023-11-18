"""n1=3456 n2=6182 n3=7610
print the fequent digit from n1,n2,n3
output:6

"""
n1,n2,n3=input().split()
s=n1+n2+n3
l=[0]*10
for i in s:
    l[int(i)]+=1
print(l.index(max(l)))
 