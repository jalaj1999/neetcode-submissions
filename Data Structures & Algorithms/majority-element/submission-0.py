class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic =dict.fromkeys(nums,0)
        ans = 0
        for num in nums:
            dic[num]+=1
            if dic[num]>(len(nums)//2):
                ans = num
        return ans
        
            