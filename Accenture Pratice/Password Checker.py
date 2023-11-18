"""
At least 4 characters 
At least one numeric digit
At Least one Capital Letter
Must not have space or slash (/)
Starting character must not be a number

Implement the function which returns 1 if given string str is valid password else 0.

Input 1:             
aA1_67

Output 1:
1

Input 2:
a987 abC012
Output 2:
0
"""
def passwordCheck(l,s):
    a=0
    d=0
    if l<4:
        return 0
    if s[0].isdigit():
        return 0
    for i in range(l):
        if s[i]==" " or s[i]=='/':
            return 0
        if s[i].isupper():
            a+=1
        if s[i].isdigit():
             d+=1
    if a>0 and d>0:
        return 1
    else:
        return 0         
             
#main
str=input()
l=len(str)
print(passwordCheck(l,str))
