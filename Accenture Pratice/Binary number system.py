"""
The Binary number system only uses two digits, 0 and 1 
and number system can be called binary string.
You are required to implement the following function:
A denotes AND operation
B denotes OR operation
C denotes XOR Operation

Input:
str: 1C0C1C1A0B1

Output:
1

Sample Input:
0C1A1B1C1C1B0A0

Output:
0
"""
str=input()
x=int(str[0])
for i in range(1,len(str),2):
    if str[i]=='A':
        x&=int(str[i+1])
    elif str[i]=='B':
        x|=int(str[i+1])
    else:
        x^=int(str[i+1])
print(x)