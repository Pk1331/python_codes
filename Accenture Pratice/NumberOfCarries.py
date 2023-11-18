"""The functions accepts two numbers num1 and num2 as its arguments. 
You are required to calculate and return  the total number of carries 
generated while adding digits of two numbers num1 and  num2.

nput
Num 1: 451
Num 2: 349
Output
2
Explanation:

Adding num1 and num2 right-to-left results in 2 carries since ( 1+9) is 10. 
1 is carried and (5+4=1) is 10, again 1 is carried. Hence 2 is returned.
"""
def NumberofCarries(n1,n2):
    carry=0
    count=0
    if len(n1)<=len(n2):
        l=len(n1)-1
    else:
        l=len(n2)-1
    for i in range(l+1):
        x=int(n1[l-i])+int(n2[l-i])+carry
        if(len(str(x))>1):
            count+=1
            carry=1
        else:
            carry=0
    return count+carry
        
#main
num1=input()
num2=input()
print(NumberofCarries(num1,num2))