class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        l = n / 3

        maj1 = 0
        maj2 = 0
        first = float('inf')
        second = float('inf')

        for i in range(0, n):
            if first == A[i]:
                maj1 += 1
            elif second == A[i]:
                maj2 += 1
            elif maj1 == 0:
                maj1 += 1
                first = A[i]
            elif maj2 == 0:
                maj2 += 1
                second = A[i]
            else:
                maj1 -= 1
                maj2 -= 1

        maj1 = 0
        maj2 = 0

        for i in range(n):
            if A[i] == first:
                maj1 += 1
            elif A[i] == second:
                maj2 += 1

        if (maj1 > l):
            return first
        if (maj2 > l):
            return second
        return -1

s = Solution()

arr = [1,3,3,1,2 ]
n = len(arr)

candidate = s.repeatedNumber(arr)

print(candidate)