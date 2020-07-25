import math

arr= [0,0,1,2,3]

n = len(arr)
arr[n-1] += 1
carry = arr[n-1]/10
arr[n-1] = arr[n-1]%10

for i in range(n-2, -1, -1):

    if (carry==1):
        arr[i] += 1
        carry = arr[i]/10
        arr[i] = arr[i]%10

if (carry==1):
    arr.insert(0,1)

while arr[0] == 0:
    del arr[0]

    # n=len(A)
    # if n<1:
    #     return [1]
    # for i in range(n-1,-1,-1):
    #     if A[i] == 9:
    #         A[i]=0
    #     else:
    #         A[i]=A[i]+1
    #         break
    # if A.count(0)==len(A): # if all values are 9 we made them 0,hence appending 1 at the front
    #     A[0]=1
    #     A.append(0)
    # k=0
    # for i in range(len(A)): # To ignore leading zeros
    #     if A[i]==0:
    #         k+=1
    #     else:
    #         break
    # return A[k:]



print(arr)