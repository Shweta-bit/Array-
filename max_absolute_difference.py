arr = [1,3,-1]
n = len(arr)
# difference =[]
# for i in range(0,n):
#     for j in range(i,n):
#         diff = (abs(arr[i]-arr[j]) + abs(i-j))
#         difference.append(diff)
# print(max(difference))

print('*'*40)

#  first = A[i] + i
# second = A[i]-i

first = [0]*n
second =[0]*n
for i in range(0,n):
    first[i] = arr[i]+i
    second[i] = arr[i]-i
first_max = max(first)
second_max= max(second)
first_min = min(first)
second_min = min(second)

ans = max(first_max-first_min, second_max-second_min)
print(ans)


