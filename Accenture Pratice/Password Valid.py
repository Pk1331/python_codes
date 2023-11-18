"""
At least 8 characters and lessthan 15c haracters
At least one numeric digit
At Least one Capital Letter
At Least one Small Letter
At Least one Special Character(!,@,#,$,%,^,&,*)
Must not have space or slash (/)
Starting character must not be a number

"""
def isValid(str,n):
    u=l=d=s=0
    sp=['@','!','%','#','$','&','*','^']
    if n>=8 and n<=15:
        if str[0].isdigit():
            return 0
        for i in range(n):
            if str[i]==" " or str[i]=='/':
                return 0
            if str[i].isupper():
                u+=1
            if str[i].islower():
                l+=1
            if str[i].isdigit():
                d+=1
            if str[i] in sp:
                s+=1
    if u>0 and l>0 and s>0 and d>0:
        return 1
    else:
        return 0
#main
str=input()
n=len(str)
res=isValid(str,n)
if res==1:
    print("Valid")
else:
    print("Invalid")
        
    