"""
The function accepts an integers arr of size length as its arguments you are required to return the sum
of second largest  element from the even positions and second smallest from the odd position of given arr

Input

arr:3 2 1 7 5 4

Output

7

Explanation

Second largest among even position elements(1 3 5) is 3
Second smallest among odd position element is 4
Thus output is 3+4 = 7

"""
def LargeSmallSum(arr,n):
    if n==0:
        return 0
    if n<=3:
        return 0
    e=[]
    o=[]
    for i in range(0,n):
        if i%2==0:
            e.append(arr[i])
        else:
            o.append(arr[i])
    e.sort(reverse=True)
    o.sort(reverse=True)
    return e[1]+o[1]  
      
#main
arr=list(map(int,input().split()))
n=len(arr)
print(LargeSmallSum(arr,n))