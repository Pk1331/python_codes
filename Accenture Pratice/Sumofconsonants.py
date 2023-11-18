"""from string if vowel has encountered  kept zero and sum the consonants elements position according to alphabets order 
s='Hello World'
output:
89

H  8
l  12
l  12
W  23
r  18
l  12
d  4
"""
str=input()
'''
s=str.lower()
v=['a','e','i','o','u',' ']
'''
s1=str.upper()
v1=['A','E','I','O','U',' ']
sum=0
for i in s1:
    if i not in v1:
        #sum+=ord(i)-96  small letters
        sum+=ord(i)-64 # Ascii values of (a-z)=(97-122) and (A-Z)=(65-90)for Example h=104-->104-96=8
print(sum)
        