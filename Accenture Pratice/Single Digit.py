"""Single digit
Num=92564
9+2+5+6+4
2+6=8
output=8

"""
def SingleDigit(n):
    sum=0
    while(n>0):
        sum+=n%10
        n=n//10
    if len(str(sum))>1:
        return SingleDigit(sum)
    else:
        return sum
    
num=int(input())
print(SingleDigit(num))
