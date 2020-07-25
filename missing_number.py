class solution:
    def missing_number(self, nums):
        if (nums == None or len(nums)==0):
            return 1
        n = len(nums)
        containsOne = 0
        # to change number>n and negative to 1
        for i in range(0,n):
            if nums[i]==1:
                containsOne =1
            elif(nums[i]<=0 or nums[i]>n):
                nums[i] = 1
        if containsOne == 0:
            return 1

        # to change all the numbers in range and flip the signs
        for i in range(0,n):
            index = abs(nums[i])-1 # to make it 0 based
            if nums[index]>0:
                nums[index] = -1*nums[index]
        # first number as positive
        for i in range(0,n):
            if (nums[i]>0):
                return  i+1

        return n+1

S = solution()
nums = [1,2,0]
print(S.missing_number(nums))







