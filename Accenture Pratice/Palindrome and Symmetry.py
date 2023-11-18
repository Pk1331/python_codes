"""
check whether the string is palindrome and symetric

step1: check palindrome 
step2: divide string in 2 equall part 
step3: first part must be equall to second part if 
step4 is valid then print palindrome and symetric else palindrome but not symetric

input:  amma
output: Palindrome and Symmetry

input : MOM
output: Palindrome but not Symmetry


"""


str=input()
n=len(str)
pali=str[::-1]
str=str.lower()
if str==pali and n%2==0:
    print("Palindrome and Symmetry")
elif str==pali and n%2!=0:
    print("Palindrome but not Symmetry")
else:
    print("Not a Palindrome but Symmetry")
    