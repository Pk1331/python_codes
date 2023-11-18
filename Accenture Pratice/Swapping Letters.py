""" 
input : Hello WoRlD

output: hELLO wOrLd

input : PaVaN kUmAR
output: pAvAn KuMar

"""
'''
#Approach-1
str=input()
print(str.swapcase())
'''
# Approach-2
str=input()
str1=""
for i in str:
    if i.islower():
        str1+=i.upper()
    else:
        str1+=i.lower()
print(str1)
        