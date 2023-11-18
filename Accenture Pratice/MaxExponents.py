"""
Example

Input:
7
12
Output:
8
Explanation:

Exponents of 2 in:

7-0

8-3

9-0

10-1

11-0

12-2

Hence maximum exponent if two is of 8.

"""
def MaxExponent(a,b):
    maxi,num=0,a
    for i in range(a,b):
        temp=Count(i)
        if temp>maxi:
            maxi,num=temp,i 
    return num
def Count(n):
    c=0
    while n%2==0 and n!=0:
        c+=1
        n= n//2
    return c
#main
a=int(input())
b=int(input())
print(MaxExponent(a,b))
