# Moore's algo
class Solution:

    def findCandidates(self, A, n):
        maj_index = 0
        count = 1

        for i in range(1, n):
            if A[maj_index] == A[i]:
                count += 1
            else:
                count -=1

            if (count==0):
                maj_index = i
                count = 1
        return A[maj_index]

    def isMAjority(self, A, n, cand):
        count = 0
        for i in range(0,n):
            if A[i] == cand:
                count +=1
        if count>int(n/2):
            return True
        else:
            return False

    def printMajority(self,A,n):
        cand = self.findCandidates(A,n)
        if (self.isMAjority(A,n,cand)):
            print(cand)
        else:
            print("no me")


g = Solution()
A = [1,3,3,1,2]
n = len(A)
cand =g.findCandidates(A,n)
print("candidate = ",cand)
# print(g.isMAjority(A,n,cand))
# g.printMajority(A,n)
