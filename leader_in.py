
# Python Function to print leaders in array
#
# def printLeaders(arr,size):
#
#     for i in range(0, size):
#         for j in range(i+1, size):
#             if arr[i]<=arr[j]:
#                 break
#         if j == size-1: # If loop didn't break
#             print ((arr[i]))
#
#         # Driver function
# arr =  [ 93, 57, 83, 41, 100, 10, 79, 27, 94, 22, 4, 96, 48, 18, 89, 37, 21, 5, 46, 81, 15, 30, 47, 23, 34, 65, 55, 9, 36, 20, 54, 17, 7, 56, 78, 84, 87, 97, 16, 69, 28, 11, 44, 49, 8, 25, 98, 75, 53, 62, 19, 24, 80, 68, 50, 91, 1, 86, 77, 14, 72, 66, 42, 63, 73, 45, 31, 61, 85, 64, 35, 32, 92, 71, 74, 3, 99, 52, 90, 43, 6, 40, 38, 2, 12, 59, 29, 82, 76, 60, 67, 13, 70, 58, 39, 33, 95, 88, 51, 26 ]
# printLeaders(arr, len(arr))

# def findleaders(array):
#     leaders = []
#     for element in array:
#         if element < leaders[-1]:
#             # new possible leader
#             leaders.append(element)
#         else:
#             # remove false possible leaders
#             while leaders[-1] < element:
#                 leaders.pop()
#                 if not leaders: break #stop when list is empty
#             leaders.append(element)
#     return leaders
#

A = [16,17,4,3,5,2]
n = len(A)

max_so_far = []
max_so_far.append(A[-1])
for i in range(n-2, -1, -1):
    if A[i] > max(max_so_far):
        max_so_far.append(A[i])

print(max_so_far)

