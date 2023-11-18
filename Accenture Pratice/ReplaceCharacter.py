str=input()
a=input()
b=input()
res=""
if len(str)==0:
    print("Null")
if a not in str and b not in str:
    print(str)
else:
    res=str.replace(a,'@').replace(b,a).replace('@',b)
print(res)
                                                   