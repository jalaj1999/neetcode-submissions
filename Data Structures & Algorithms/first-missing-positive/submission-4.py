class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)+1
        check = [0]*n
        print(check)
        for num in nums:
            if num>=n or num<0:
                continue
            check[num]+=1
        for i in range(1,len(check)):
            if check[i] ==0:
                return i
        return n
        