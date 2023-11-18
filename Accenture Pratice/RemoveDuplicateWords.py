'''
Exp-1
input   : he is playing football and he is summing and enjoying summer vacation
outpiut : he is playing football and summing enjoying summner vacation

Exp-2
input  : She is dancer and She is Coreographer and She is feminist also
output : She is dancer and Coreographer feminist also  
'''
#approach-1

str=input().split()
l=[]
for i in str:
    if i not in l:
        l.append(i)
print(" ".join(l))


# approach-2
'''
str=input().split()
s=set()
for i in str:
    if i not in s:
        print(i,end=' ')
        s.add(i)
'''
        
