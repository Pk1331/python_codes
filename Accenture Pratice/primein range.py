def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

a=int(input())
i=0
c=0
while c!=a:
    i+=1
    if is_prime(i):
        c+=1
print(i)

    
    
    