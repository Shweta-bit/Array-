class Solution:
    def findPerm(self, s, n):
        max = n
        min = 1
        res = [None]*n
        Stack = []
        j = 0
        for i in range(1,n):
            if (s[i-1] == "I"):
                Stack.append(i)
                while(Stack):

                    res[j] = Stack.pop()
                    j += 1
            else:
                Stack.append(i)
        Stack.append(n)
        while(Stack):

            res[j] = Stack.pop()
            j +=1
        return res

        #         max -=1
        #     else:
        #         res.append(min)
        #         min+=1
        # res.append(max)
        # res.reverse()
        # return res
g = Solution()
print(g.findPerm("DDIIIID",8))
