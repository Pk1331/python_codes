"""nput
n: 12
num: 718

Output
4BA

Explanation
num         Divisor          quotient              remainder
718           12               59                   10(A)
59            12                4                   11(B)
4             12                0                   4(4)


"""


def N_base_notation(num,n):
    res=""
    while num>0:
        rem=num%n
        if rem>9:
            res+=chr(rem+55)
        else:
            res+=str(rem)
        num=num//n
    return res[::-1]
#main
num=int(input())
n=int(input())
print(N_base_notation(num,n))