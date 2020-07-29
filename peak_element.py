a = [ 9488, 25784, 5652, 9861, 31311, 8611, 1671, 7129, 28183, 2743, 11059, 4473, 7927, 21287, 2259, 7214, 32529 ]
# n = len(a)
# for i in range(1,n-1):
#     for j in range(0,n):
#         if a[i]> a[j] and a[i]<a[j+2]:
#             print("1")
#             break
class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, a):
        n = len(a)
        leftmax = [None]*n
        leftmax[0] = float('-inf')

        for i in range(1,n):
            leftmax[i] = max(leftmax[i-1], a[i-1])

        rightmin = [None]*n
        rightmin[-1] = float('inf')
        for i in range(n-2,-1,-1):
            rightmin[i] = min(rightmin[i+1], a[i+1])

        for i in range(1,n-1):
            if leftmax[i] < a[i] and rightmin[i]> a[i]:
                return 1

            #rightmin = min(rightmin, a[i])
        return 0
n = len(a)
print(findElement(a,n))