"""
input :121
output :121

input:57
output:363

Explanation: 57 not a palindrome then 57+75=132 again check palindrome 132 is not a palindrome therfore 132+231=363
363 is palindrome so result is 363

 
"""
n=int(input())
x=str(n)
while(x!=x[::-1]):
    n=n+int(x[::-1])
    x=str(n)
print(n)