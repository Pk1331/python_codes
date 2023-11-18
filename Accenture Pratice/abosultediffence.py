"""
The function accepts an integer array arr, its length and two integer variables num and diff. Implement this function to find and return the number of elements of ‘arr’ having an absolute difference of less than or equal to ‘diff’ with ‘num’.
Note: In case there is no element in arr whose absolute difference with num is less than or equal to diff, return -1.

Example:

Input:

arr: 12 3 14 56 77 13
num: 13
diff: 2
Output:3

"""
def findCount(arr,num,diff,n):
    if n==0:
        return -1
    else:
        count=0
        for i in range(n):
            res=abs(arr[i]-num)
            if(res<=diff):
                count+=1
        return count
#main
arr=list(map(int,input().split()))
num=int(input())
diff=int(input())
n=len(arr)
print(findCount(arr,num,diff,n))