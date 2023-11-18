"""
input:
r=7(no of rats)
unit=2 (no of units each rate consume)
n=8
arr=2 8 3 5 7 4 1 2

output:
4

Explanation:
total amount of food r*unit=7*2=14
2+8+3+5=18
18-14=4

Ex-2
r=6 u=2 n=8 arr= 2 8 3 5 7 4 1 2 
Explanation:
   r*u=6*2=12
   2+8+3=13
   13-12=1
   
   output: 1

"""
rats=int(input())
units=int(input())
n=int(input())
arr=list(map(int,input().split()))
total=rats*units
sum=0
for i in range(n):
    if n==0:
        res=-1
    sum+=arr[i]
    if sum>=total:
        res=sum-total
        break
    else:
        res=0
print(res)