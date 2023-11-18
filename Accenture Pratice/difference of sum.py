"""
The function accepts two integers n, m as arguments Find the sum of all numbers 
n range from 1 to m(both inclusive) that are not divisible by n. Return difference 
between sum of integers not divisible by n with sum of numbers divisible by n


Input
n:4
m:20
Output
90

Explanation
Sum of numbers divisible by 4 are 4 + 8 + 12 + 16 + 20 = 60
Sum of numbers not divisible by 4 are 1 +2 + 3 + 5 + 6 + 7 + 9 + 10 + 11 + 13 + 14 + 15 + 17 + 18 + 19 = 150
Difference 150 - 60 = 90

"""
def differnceSum(n,m):
    dv=ndv=0
    for i in range(1,m+1):
        if i%n==0:
            dv+=i
        else:
            ndv+=i
    return ndv-dv
#main
n=int(input())
m=int(input())
print(differnceSum(n,m))