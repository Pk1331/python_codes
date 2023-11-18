"""N= 532 arr=['PNP'] 
-->if letter is p add digits
-->if letter is n subtract digits
sum=0 0+5=5 5-3=2 sum 2+2=4
res=sum*100 =400 """
num=input()
str=input()
sum=0
for i in range(len(num)):
    if str[i]=='P':
        sum+=int(num[i])
    if str[i]=='N':
        sum-=int(num[i])
print(sum*100)
    