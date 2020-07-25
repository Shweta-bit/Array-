class Solution:
    def repeatnumbers(self,A):
        A_repeated_twice = sum(A) - sum(set(A))
        print(A_repeated_twice)
        n = len(A)
        sum_n = int((n*(n+1))/2)
        B_missing = sum_n - sum(set(A))
        print(B_missing)
        return A_repeated_twice, B_missing



g = Solution()
A = [3,1,2,5,3]
print(g.repeatnumbers(A))

        # A = [3,1,2,5,3]
        # sort it out [1,2,3,3,5]
        # set of array set(A) = 1,2,3,5
        # sum of element(A) = [1,2,3,3,5] = 14
        # sum of set(A) = [1,2,3,5] = 11
        # sum of set(A) - sum of array(A) = ans





