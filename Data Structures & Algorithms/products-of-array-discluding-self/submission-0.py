class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left ,right =[],[]
        p =1
        for num in nums:
            p*=num
            left.append(p)
        
        p =1
        for num in reversed(nums):
            p*=num
            right.append(p)
        right.reverse()
        
        ans =[]
        for i in range(len(nums)):
            if i ==0:
                ans.append(right[1])
                continue
            if i == len(nums)-1:
                ans.append(left[-2])
                continue
            ans.append(left[i-1]*right[i+1])
            
        return ans

            