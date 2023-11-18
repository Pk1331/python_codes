"""from string if vowel has encountered  kept zero and sum the consonants elements position according to alphabets order 
s='Hello World'
output:
35

e 5
0 15
0 15

"""
s=input()
s1=s.lower()
v=['a','e','i','o','u']
sum=0
for i in s1:
    if i in v:
        sum+=ord(i)-96
print(sum)